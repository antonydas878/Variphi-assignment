# models/clip_model.py

import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def encode_image(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    
    with torch.no_grad():
        embedding = model.encode_image(image)
    
    return embedding / embedding.norm(dim=-1, keepdim=True)