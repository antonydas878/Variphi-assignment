# api/app.py

from fastapi import FastAPI
from query.retriever import search
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
app = FastAPI()

@app.get("/search")
def query(q: str):
    results = search(q)
    return {"results": results}