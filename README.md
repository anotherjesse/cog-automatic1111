# building

inside of the cog

    cog run /bin/bash

run `./install.sh` to install the dependencies

    ./install.sh

Then ensure that the webui has all its dependencies installed

    ./webui.sh --listen --port 7860 --api --no-download-sd-model

Then fix the fact it doesn't install the right tqdm / xformers

    cd stable-diffusion-webui 
    source venv/bin/active
    pip install -U tqdm xformers

## errors that still exist

"Warning: Failed to install svglib, some preprocessors may not work."

  Downloading pycairo-1.23.0.tar.gz (344 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 344.6/344.6 KB 39.8 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Installing backend dependencies: started
  Installing backend dependencies: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: svglib, pycairo
  Building wheel for svglib (setup.py): started
  Building wheel for svglib (setup.py): finished with status 'done'
  Created wheel for svglib: filename=svglib-1.5.1-py3-none-any.whl size=30905 sha256=e55082ae1d77c354023cb851f4a63343abef4a105262a2b5e1259e7dbd06c229
  Stored in directory: /root/.cache/pip/wheels/63/be/8a/04843287552b727babbb0e6de7d646d0e0728536f4a5f7ca1c
  Building wheel for pycairo (pyproject.toml): started
  Building wheel for pycairo (pyproject.toml): finished with status 'error'
Successfully built svglib
Failed to build pycairo

stderr:   error: subprocess-exited-with-error
  
  × Building wheel for pycairo (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [15 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.linux-x86_64-cpython-38
      creating build/lib.linux-x86_64-cpython-38/cairo
      copying cairo/__init__.py -> build/lib.linux-x86_64-cpython-38/cairo
      copying cairo/__init__.pyi -> build/lib.linux-x86_64-cpython-38/cairo
      copying cairo/py.typed -> build/lib.linux-x86_64-cpython-38/cairo
      running build_ext
      Package cairo was not found in the pkg-config search path.
      Perhaps you should add the directory containing `cairo.pc'
      to the PKG_CONFIG_PATH environment variable
      No package 'cairo' found
      Command '['pkg-config', '--print-errors', '--exists', 'cairo >= 1.15.10']' returned non-zero exit status 1.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pycairo
ERROR: Could not build wheels for pycairo, which is required to install pyproject.toml-based projects
WARNING: You are using pip version 22.0.4; however, version 23.1.2 is available.
You should consider upgrading via the '/src/stable-diffusion-webui/venv/bin/python3 -m pip install --upgrade pip' command.

Warning: Failed to install svglib, some preprocessors may not work.