import streamlit as st

from utils.config import (
    COMPANY,
    VERSION,
)


def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title("🤖 AI Knowledge Assistant")

        st.divider()

        st.markdown(
            f"**Application**  \n"
            f"{COMPANY}"
        )

        st.markdown(
            f"**Version**  \n"
            f"{VERSION}"
        )

        st.divider()

        st.success(
            "Knowledge Base Loaded"
        )

        st.info(
            "Enterprise Payroll FAQ"
        )

        st.divider()

        st.caption(
            "Built using:\n"
            "- Python\n"
            "- Streamlit\n"
            "- FastAPI\n"
            "- Azure OpenAI\n"
            "- ChromaDB"
        )