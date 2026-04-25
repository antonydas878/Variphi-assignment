# query/retriever.py

import json
import numpy as np
from sklearn.neighbors import NearestNeighbors
from models.clip_model import model
import torch
import clip

# Load stored embeddings (you must save them as .npy during indexing)
embeddings = np.load("index/embeddings.npy")

nn = NearestNeighbors(n_neighbors=5, metric='cosine')
nn.fit(embeddings)

def search(query_text, top_k=5):
    text_tokens = clip.tokenize([query_text])

    with torch.no_grad():
        query_embedding = model.encode_text(text_tokens)

    query_embedding = query_embedding / query_embedding.norm(dim=-1, keepdim=True)
    query_embedding = query_embedding.cpu().numpy()

    distances, indices = nn.kneighbors(query_embedding, n_neighbors=top_k)

    with open("index/metadata.json") as f:
        metadata = json.load(f)

    results = []
    for idx, dist in zip(indices[0], distances[0]):
        results.append({
            "frame": metadata[idx]["path"],
            "timestamp": metadata[idx]["time"],
            "score": float(1 - dist)
        })

    return results