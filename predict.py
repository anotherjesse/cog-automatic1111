import os
import shutil
from typing import Iterator

from cog import BasePredictor, Input, Path
import random
import subprocess
import time
import requests

import webuiapi


class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        self.port = 7860
        # fixme(ja): this script probably is doing too much, we can probably just skip directly to launching?
        self.daemon = subprocess.Popen(["./webui.sh", "--listen", "--port", str(self.port), "--api", "--no-download-sd-model"], cwd="./stable-diffusion-webui")

        # Wait for the server to start
        start = time.time()
        while True:
            try:
                requests.get(f"http://localhost:{self.port}/")
                break
            except requests.exceptions.ConnectionError:
                if time.time() - start > 60:
                    raise RuntimeError("Server failed to start")
                time.sleep(0.1)

        print("startup complete, duration:", time.time() - start)

        # FIXME(ja): seems like you need to let it sleep a little more after it starts listening on the port
        time.sleep(5)

        self.api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)


    def predict(
        self,
        prompt: str = Input(
            description="Input prompt",
            default="photo of cjw person",
        ),
        negative_prompt: str = Input(
            description="Specify things to not see in the output",
            default=None,
        ),
        steps: int = Input(
            description="Number of denoising steps", ge=1, le=500, default=50
        ),
        cfg_scale: float = Input(
            description="Scale for classifier-free guidance", ge=1, le=20, default=7.5
        ),
        
        seed: int = Input(
            description="Random seed. Leave blank to randomize the seed", default=None
        ),
    ) -> Iterator[Path]:
        """Run a single prediction on the model"""

        if not seed:
            seed = random.randint(0, 2 ** 32 - 1)

        status = self.daemon.poll()

        # poll returns None if the process is still running
        if status is None:
            print("Process is still running")
        # Otherwise it returns the process's exit code. 0 usually means that the process has completed without errors
        elif status == 0:
            print("Process finished successfully")
        else:
            print("Process terminated with error. Exit code:", status)

        result = self.api.txt2img(prompt=prompt,
                            negative_prompt=negative_prompt,
                            seed=seed,
                            # styles=["anime"],
                            cfg_scale=cfg_scale,
                            steps=steps)

        for idx, image in enumerate(result.images):
            image.save(f"output_{idx}.png")
            yield Path(f"output_{idx}.png")