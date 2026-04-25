# pipeline/index_builder.py

import faiss
import numpy as np
import json

def build_index(embeddings, metadata):
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, "index/faiss_index.bin")

    with open("index/metadata.json", "w") as f:
        json.dump(metadata, f)