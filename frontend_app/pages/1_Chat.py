import streamlit as st
from pathlib import Path
import sys
from components.chat import render_chat
from app.services.rag_services import RAGService

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    

st.title("💬 AI Knowledge Assistant")

st.write(
    "Ask questions about the Enterprise Payroll Knowledge Base."
)

st.divider()

render_chat()