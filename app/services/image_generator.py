from diffusers import StableDiffusionPipeline
import torch
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

# "cuda" if torch.cuda.is_available() else "cpu" - auto

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda") # or pipe.to(device)
#pipe.enable_xformers_memory_efficient_attention()

def generate_image(
        prompt: str,
        image_id: str,
        output_dir: str = "static/images",
        steps: int = 25
) -> dict:
    os.makedirs(output_dir, exist_ok=True)

    try:
        image = pipe(prompt, num_inference_steps=steps).images[0]
        filepath = os.path.join(output_dir, f"{image_id}.png")
        image.save(filepath)
    except Exception as e:
        print(f"[ERROR] Failed to generate image: {e}")
