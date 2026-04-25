# pipeline/temporal_context.py

import numpy as np

def add_temporal_context(embeddings, window=2):
    new_embeddings = []

    for i in range(len(embeddings)):
        start = max(0, i - window)
        end = min(len(embeddings), i + window + 1)

        context = np.mean(embeddings[start:end], axis=0)
        new_embeddings.append(context)

    return np.array(new_embeddings)