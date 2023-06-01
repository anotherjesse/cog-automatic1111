#!/bin/bash

# install A1111's stable-diffusion-webui
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

# install extensions
git clone https://github.com/hako-mikan/sd-webui-regional-prompter.git stable-diffusion-webui/extensions/sd-webui-regional-prompter
git clone https://github.com/Mikubill/sd-webui-controlnet.git stable-diffusion-webui/extensions/sd-webui-controlnet
git clone https://github.com/deforum-art/sd-webui-modelscope-text2video.git stable-diffusion-webui/extensions/sd-webui-modelscope-text2video
git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111.git stable-diffusion-webui/extensions/ultimate-upscale-for-automatic1111

cp config.json stable-diffusion-webui/config.json

TARGET_DIR="stable-diffusion-webui/models/Stable-diffusion"
URLS=(
"https://huggingface.co/XpucT/Deliberate/resolve/main/Deliberate_v2.safetensors"
)

for url in "${URLS[@]}"; do
  wget --no-verbose -P "$TARGET_DIR" "$url"
done

# install Controlnet models and t2iadapters
# https://github.com/TheLastBen/fast-stable-diffusion/blob/main/AUTOMATIC1111_files/CN_models.txt
TARGET_DIR="stable-diffusion-webui/extensions/sd-webui-controlnet/models"
URLS=(
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime.pth"
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_keypose-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_seg-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_sketch-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_depth-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_canny-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_color-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_style-fp16.safetensors"
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_openpose-fp16.safetensors"
)

mkdir -p "$TARGET_DIR"
for url in "${URLS[@]}"; do
  wget --no-verbose -P "$TARGET_DIR" "$url"
done

TARGET_DIR="stable-diffusion-webui/models/ModelScope/t2v"
URLS=(
"https://huggingface.co/kabachuha/modelscope-damo-text2video-pruned-weights/resolve/main/VQGAN_autoencoder.pth"
"https://huggingface.co/kabachuha/modelscope-damo-text2video-pruned-weights/resolve/main/open_clip_pytorch_model.bin"
"https://huggingface.co/kabachuha/modelscope-damo-text2video-pruned-weights/resolve/main/text2video_pytorch_model.pth"
"https://huggingface.co/kabachuha/modelscope-damo-text2video-pruned-weights/resolve/main/configuration.json"
)

mkdir -p "$TARGET_DIR"
for url in "${URLS[@]}"; do
  wget --no-verbose -P "$TARGET_DIR" "$url"
done
