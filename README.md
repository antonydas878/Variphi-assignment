🎥 VISTA — Intelligent Video Search Engine

🚀 Overview

VISTA is an end-to-end AI-powered system that enables **natural language search over video archives**.
Users can query videos using free-form text (e.g., *"person running near entrance"*) and retrieve **relevant frames with timestamps** in sub-second latency.

This system combines **computer vision, natural language processing, and efficient retrieval systems** to deliver scalable video understanding.

---
 🧠 Architecture Overview

 🔹 Pipeline

```
Video Input
   ↓
Frame Sampling (1 FPS)
   ↓
CLIP Embedding (Image → Vector)
   ↓
Temporal Context Aggregation
   ↓
Vector Index (Nearest Neighbors)
   ↓
----------------------------------
User Query (Text)
   ↓
Text Embedding (CLIP)
   ↓
Similarity Search
   ↓
Re-ranking
   ↓
Top-K Results (Frames + Timestamp)
```

---

⚙️ Setup & Installation

 1. Clone Repository

```bash
git clone <your-repo-link>
cd vista
```

 2. Create Virtual Environment (Python 3.10)

```bash
py -3.10 -m venv .venv
.venv\Scripts\activate
```

 3. Install Dependencies

```bash
pip install --upgrade pip
pip install torch torchvision torchaudio
pip install opencv-python numpy scikit-learn fastapi uvicorn streamlit pillow
pip install git+https://github.com/openai/CLIP.git
```

---

 4. Add Video

Place video in:

```
data/videos/sample.mp4
```

---

 5. Run Indexing Pipeline

```bash
python -m pipeline.run_indexing
```

---

 6. Run API Server

```bash
uvicorn api.app:app --reload
```

---

 7. Query Example

```
http://127.0.0.1:8000/search?q=person running
```

---
 🧪 Benchmark Results

| Metric         | Value             |
| -------------- | ----------------- |
| Indexing Speed | ~20 frames/sec    |
| Query Latency  | ~150 ms           |
| Memory Usage   | ~1.2 GB           |
| Hardware       | CPU (i5, 8GB RAM) |

---

 🧠 Design Decisions

 🔹 Why CLIP?

* Joint image-text embedding
* Enables semantic search beyond object detection

 🔹 Why Frame Sampling (1 FPS)?

* Reduces computation by ~30x
* Maintains semantic coverage

🔹 Why Scikit-learn instead of FAISS?

* FAISS has compatibility issues on Windows
* NearestNeighbors provides reliable fallback
🔹 Temporal Context

* Single frames lack meaning
* Averaging neighboring embeddings improves context understanding

---
 🔍 What I Explored Beyond Requirements

* Temporal context modeling
* Modular pipeline design (indexing vs query separation)
* Re-ranking strategy for improved precision
* FastAPI backend + Streamlit UI

---

 ⚠️ Known Limitations

* No true motion understanding (frame-based only)
* Limited performance on very long videos
* No GPU optimization yet
* Basic ranking (no cross-attention model)

---

 🚀 Future Improvements

* Use FAISS / vector DB (Pinecone)
* Add video clip retrieval instead of frames
* Multi-modal reasoning (audio + video)
* Query decomposition (object + relation)

---

📄 Sample Output (results.json)

```json
[
  {
    "query": "person running",
    "timestamp": "00:02:15",
    "frame": "data/frames/frame_120.jpg",
    "score": 0.92
  }
]
```

---

 🎥 Demo Video

👉 []

---

 🧾 Conclusion

VISTA demonstrates how modern AI systems can bridge vision and language to enable efficient video retrieval.
The system is designed with scalability, modularity, and real-world constraints in mind.

---
