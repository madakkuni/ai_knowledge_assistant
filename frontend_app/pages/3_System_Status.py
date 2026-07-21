"""
System Status Dashboard.

Displays application health, AI configuration,
and knowledge base statistics.
"""

import sys
from pathlib import Path

import streamlit as st

# -------------------------------------------------------------------
# Add project root to Python path
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# -------------------------------------------------------------------
# Application Imports
# -------------------------------------------------------------------

from app.services.system_status_service import (
    SystemStatusService,
)

# -------------------------------------------------------------------
# Page Configuration
# -------------------------------------------------------------------

st.set_page_config(
    page_title="System Status",
    page_icon="🖥️",
    layout="wide",
)

# -------------------------------------------------------------------
# Load Status
# -------------------------------------------------------------------

service = SystemStatusService()

status = service.get_status()

# -------------------------------------------------------------------
# Page Header
# -------------------------------------------------------------------

st.title("🖥️ AI System Dashboard")

st.caption(
    "Enterprise Retrieval-Augmented Generation (RAG) Application"
)

# -------------------------------------------------------------------
# Health Indicator
# -------------------------------------------------------------------

if status["status"] == "Healthy":
    st.success("🟢 System Status : Healthy")
else:
    st.error("🔴 System Status : Unavailable")

st.divider()

# -------------------------------------------------------------------
# Summary Cards
# -------------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        label="📄 Documents",
        value=status["documents_indexed"],
    )

with col2:

    st.metric(
        label="🧩 Chunks",
        value=status["chunks_indexed"],
    )

with col3:

    st.metric(
        label="🌍 Environment",
        value=status["environment"],
    )

with col4:

    st.metric(
        label="✅ Status",
        value=status["status"],
    )

st.divider()

# -------------------------------------------------------------------
# Application Information
# -------------------------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📦 Application")

    st.info(
        f"""
**Application**

{status["application_name"]}

---

**Version**

{status["application_version"]}

---

**Environment**

{status["environment"]}
"""
    )

with right:

    st.subheader("🤖 AI Configuration")

    st.info(
        f"""
**Chat Model**

{status["chat_model"]}

---

**Embedding Model**

{status["embedding_model"]}

---

**Vector Store**

{status["vector_store"]}

---

**Chunk Strategy**

{status["chunk_strategy"]}
"""
    )

st.divider()

# -------------------------------------------------------------------
# Knowledge Base Summary
# -------------------------------------------------------------------

st.subheader("📚 Knowledge Base")

kb_col1, kb_col2 = st.columns(2)

with kb_col1:

    st.metric(
        label="Indexed Documents",
        value=status["documents_indexed"],
    )

with kb_col2:

    st.metric(
        label="Indexed Chunks",
        value=status["chunks_indexed"],
    )

st.divider()

# -------------------------------------------------------------------
# Raw Configuration
# -------------------------------------------------------------------

with st.expander("⚙️ View System Details"):

    st.json(status)

# -------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------

st.caption(
    "AI Knowledge Assistant • Enterprise RAG Demo"
)