import time

import streamlit as st

import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.services.rag_services import RAGService


def render_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    rag_service = RAGService()

    # Display previous conversation
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask a question about the knowledge base..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        start = time.perf_counter()

        with st.spinner("Searching knowledge base..."):

            answer = rag_service.generate_answer(prompt)

        elapsed = time.perf_counter() - start

        with st.chat_message("assistant"):

            st.markdown(answer)

            st.caption(
                f"Response generated in {elapsed:.2f} sec"
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )