import os
import shutil
from typing import Iterator

from cog import BasePredictor, Input, Path
import subprocess


class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        self.port = 7860
        self.daemon = subprocess.Popen(["./webui.sh", "--listen", "--port", str(self.port), "--api", "--no-download-sd-model"], cwd="./stable-diffusion-webui")

    def predict(
        self,
        control_image: Path = Input(
            description="Optional Image to use for guidance based on canny",
            default=None,
        ),
        image: Path = Input(
            description="Optional Image to use for img2img guidance", default=None
        ),
        mask: Path = Input(
            description="Optional Mask to use for legacy inpainting", default=None
        ),
        prompt: str = Input(
            description="Input prompt",
            default="photo of cjw person",
        ),
        negative_prompt: str = Input(
            description="Specify things to not see in the output",
            default=None,
        ),
        width: int = Input(
            description="Width of output image. Maximum size is 1024x768 or 768x1024 because of memory limits",
            choices=[128, 256, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960, 1024],
            default=512,
        ),
        height: int = Input(
            description="Height of output image. Maximum size is 1024x768 or 768x1024 because of memory limits",
            choices=[128, 256, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960, 1024],
            default=512,
        ),
        num_outputs: int = Input(
            description="Number of images to output.",
            ge=1,
            le=10,
            default=1,
        ),
        num_inference_steps: int = Input(
            description="Number of denoising steps", ge=1, le=500, default=50
        ),
        guidance_scale: float = Input(
            description="Scale for classifier-free guidance", ge=1, le=20, default=7.5
        ),
        prompt_strength: float = Input(
            description="Prompt strength when using init image. 1.0 corresponds to full destruction of information in init image",
            default=0.8,
        ),
        low_threshold: int = Input(
            description="Low threshold for canny filter", default=100
        ),
        high_threshold: int = Input(
            description="High threshold for canny filter", default=200
        ),
        scheduler: str = Input(
            default="DPMSolverMultistep",
            choices=[
                "DDIM",
                "DPMSolverMultistep",
                "HeunDiscrete",
                "K_EULER_ANCESTRAL",
                "K_EULER",
                "KLMS",
                "PNDM",
                "UniPCMultistep",
            ],
            description="Choose a scheduler.",
        ),
        disable_safety_check: bool = Input(
            description="Disable safety check. Use at your own risk!", default=False
        ),
        return_processed_control: bool = Input(
            description="if using control_image, return processed control as first image", default=False
        ),
        seed: int = Input(
            description="Random seed. Leave blank to randomize the seed", default=None
        ),
    ) -> Iterator[Path]:
        """Run a single prediction on the model"""

        status = self.daemon.poll()

        # poll returns None if the process is still running
        if status is None:
            print("Process is still running")
        # Otherwise it returns the process's exit code. 0 usually means that the process has completed without errors
        elif status == 0:
            print("Process finished successfully")
        else:
            print("Process terminated with error. Exit code:", status)

