import os
import streamlit as st

from src.rag_chain import ask
from src.ingest import ingest_pdf
from src.document_registry import get_document_names
from src.vector_store import delete_document

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Automotive AI Buddy",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed" not in st.session_state:
    st.session_state.processed = False

if "current_file" not in st.session_state:
    st.session_state.current_file = None

# -----------------------------
# Header
# -----------------------------
st.title("Document Inteligence Platform")
st.caption("Upload any PDF and chat with it using Azure OpenAI + MongoDB RAG")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Document Inteligence")
st.sidebar.markdown("---")

uploaded_files = st.sidebar.file_uploader(
    "📄 Upload PDF(s)",
    type=["pdf"],
    accept_multiple_files = True
)

if uploaded_files:

    st.sidebar.write("### Uploaded PDFs")

    for file in uploaded_files:
        st.sidebar.write(f"📄 {file.name}")

    if st.sidebar.button("Process PDFs"):

        os.makedirs("uploads", exist_ok=True)

        total_chunks = 0
        processed = 0
        skipped = 0

        with st.spinner("Generating embeddings..."):

            for file in uploaded_files:

                file_path = os.path.join(
                    "uploads",
                    file.name
                )

                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())

                result = ingest_pdf(file_path)

                if result["status"] == "processed":

                    processed += 1
                    total_chunks += result["chunks"]

                    st.sidebar.success(
                        f"✅ {result['document']} indexed ({result['chunks']} chunks)"
                    )

                else:

                    skipped += 1

                    st.sidebar.info(
                        f"{result['document']} already indexed. Skipped."
                    )

        st.session_state.processed = True

        st.sidebar.success(
            f"Finished: {processed} processed | {skipped} skipped | {total_chunks} chunks added"
        )

documents = ["All Documents"] + get_document_names()
selected_document = st.sidebar.selectbox("Search In", documents)

st.sidebar.markdown("---")
st.sidebar.subheader("🗑 Delete Document")

documents_to_delete = get_document_names()

if documents_to_delete:

    delete_doc = st.sidebar.selectbox(
        "Select document",
        documents_to_delete,
        key="delete_doc"
    )

    if st.sidebar.button("Delete Document"):

        if delete_document(delete_doc):

            st.sidebar.success(
                f"Deleted {delete_doc}"
            )

            st.rerun()

        else:

            st.sidebar.error(
                "Document not found."
            )

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []
    st.rerun()

# -----------------------------
# Welcome Screen
# -----------------------------
if (
    len(st.session_state.messages) == 0
    and not st.session_state.processed
):

    st.markdown("""
# 👋 Welcome!

Upload a PDF, click **Process PDF**, and start chatting.

Try asking any Question:

""")

# -----------------------------
# Display Previous Chat
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            st.caption("📄 Sources")

            shown = set()

            for source in message["sources"]:

                key = (source["document"], source["page"])

                if key not in shown:

                    shown.add(key)

                    st.caption(
                    f"• {source['document']} - Page {source['page']}"
                )

# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input(
    "Ask anything about the uploaded document..."
)

if question:

    if not st.session_state.processed:

        st.warning("⚠️ Please upload and process a PDF first.")
        st.stop()

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = ask(question, selected_document)

            answer = result["answer"]
            sources = result["sources"]

        st.markdown(answer)

        shown = set()

        st.caption("📄 Sources")

        for source in sources:

            key = (source["document"], source["page"])

            if key not in shown:

                shown.add(key)

                st.caption(
                    f"• {source['document']} - Page {source['page']}"
                )


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )
    