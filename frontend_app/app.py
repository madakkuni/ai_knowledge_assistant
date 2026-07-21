import streamlit as st

from components.sidebar import render_sidebar
from utils.config import (
    APP_ICON,
    APP_TITLE,
    DESCRIPTION,
)

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
)

render_sidebar()

st.title("🤖 AI Knowledge Assistant")

st.markdown(DESCRIPTION)

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Knowledge Base",
        "Enterprise Payroll FAQ",
    )

with col2:

    st.metric(
        "Status",
        "Ready",
    )

st.divider()

st.subheader("Project Overview")

st.markdown(
    """
This application demonstrates an Enterprise
Retrieval-Augmented Generation (RAG) solution.

Current capabilities:

- Document Ingestion
- FAQ Chunking
- Azure OpenAI Embeddings
- ChromaDB Vector Store
- Semantic Retrieval
- Prompt Builder
- GPT Chat Completion
"""
)

st.info(
    "Use the navigation menu on the left to explore the application."
)