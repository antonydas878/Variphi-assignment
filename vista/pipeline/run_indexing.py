# pipeline/run_indexing.py

import os
import numpy as np
import json
from pipeline.frame_sampler import sample_frames
from models.clip_model import encode_image

VIDEO_PATH = "data/videos/sample.mp4"
FRAMES_DIR = "data/frames"
INDEX_DIR = "index"

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)

print("Step 1: Sampling frames...")
sample_frames(VIDEO_PATH, FRAMES_DIR, sample_rate=1)

print("Step 2: Generating embeddings...")

embeddings = []
metadata = []

for i, frame_file in enumerate(sorted(os.listdir(FRAMES_DIR))):
    path = os.path.join(FRAMES_DIR, frame_file)

    emb = encode_image(path).cpu().numpy()[0]
    embeddings.append(emb)

    metadata.append({
        "path": path,
        "time": f"{i:02d}:00"
    })

embeddings = np.array(embeddings)

print("Step 3: Saving index...")

np.save("index/embeddings.npy", embeddings)

with open("index/metadata.json", "w") as f:
    json.dump(metadata, f)

print("✅ Indexing complete!")
