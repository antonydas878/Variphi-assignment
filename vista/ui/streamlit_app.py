# ui/streamlit_app.py

import streamlit as st
import requests

st.title("VISTA - Video Search")

query = st.text_input("Enter query")

if st.button("Search"):
    res = requests.get(f"http://localhost:8000/search?q={query}")
    data = res.json()

    for r in data["results"]:
        st.image(r["frame"])
        st.write(f"Time: {r['timestamp']}")
        st.write(f"Score: {r['score']}")