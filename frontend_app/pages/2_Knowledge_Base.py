"""
Knowledge Base Explorer.

Browse and search indexed knowledge chunks.
"""

import sys
from pathlib import Path

import streamlit as st

# ------------------------------------------------------------------
# Add Project Root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ------------------------------------------------------------------
# Application Imports
# ------------------------------------------------------------------

from app.services.knowledge_base_service import (
    KnowledgeBaseService,
)

# ------------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------------

st.set_page_config(
    page_title="Knowledge Base",
    page_icon="📚",
    layout="wide",
)

# ------------------------------------------------------------------
# Header
# ------------------------------------------------------------------

header1, header2 = st.columns([8, 1])

with header1:

    st.title("📚 Knowledge Base Explorer")

    st.caption(
        "Browse and search indexed knowledge chunks."
    )

with header2:

    if st.button(
        "🔄 Refresh",
        use_container_width=True,
    ):
        st.rerun()

# ------------------------------------------------------------------
# Load Chunks
# ------------------------------------------------------------------

service = KnowledgeBaseService()

chunks = service.get_chunks()

# ------------------------------------------------------------------
# Search
# ------------------------------------------------------------------

search = st.text_input(
    "🔍 Search Knowledge Base",
    placeholder="Search by question, source or content...",
)

if search:

    keyword = search.lower()

    filtered_chunks = []

    for chunk in chunks:

        metadata = chunk.get(
            "metadata",
            {}
        )

        question = metadata.get(
            "question",
            ""
        ).lower()

        source = metadata.get(
            "source",
            ""
        ).lower()

        content = chunk.get(
            "content",
            ""
        ).lower()

        if (
            keyword in question
            or keyword in source
            or keyword in content
        ):
            filtered_chunks.append(
                chunk
            )

    chunks = filtered_chunks

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------

st.success(
    f"Found **{len(chunks)}** chunk(s)."
)

st.divider()

# ------------------------------------------------------------------
# Display Chunks
# ------------------------------------------------------------------

if not chunks:

    st.warning(
        "No matching chunks found."
    )

else:

    for chunk in chunks:

        metadata = chunk.get(
            "metadata",
            {}
        )

        title = (
            f"📄 Chunk "
            f"{metadata.get('chunk_id','-')} "
            f"- "
            f"{metadata.get('question','No Question')}"
        )

        with st.expander(title):

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### Question")

                st.write(
                    metadata.get(
                        "question",
                        "N/A",
                    )
                )

            with col2:

                st.markdown("### Source")

                st.write(
                    metadata.get(
                        "source",
                        "N/A",
                    )
                )

            st.markdown("---")

            st.markdown("### Content")

            st.write(
                chunk.get(
                    "content",
                    "",
                )
            )

            st.markdown("---")

            st.caption(
                f"Chunk ID : "
                f"{metadata.get('chunk_id','-')}"
            )

# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------

st.divider()

st.caption(
    "AI Knowledge Assistant | Knowledge Base Explorer"
)