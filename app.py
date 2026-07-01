import os
import streamlit as st

from src.retrieval.rag_chain import ask
from src.ingestion.ingest import ingest_pdf
from src.storage.document_registry import get_document_names
from src.storage.vector_store import delete_document
from src.memory.chat_history import (start_new_chat,
                                    get_all_chats,
                                    get_chat_history,
                                    add_user_message,
                                    add_assistant_message,
                                    clear_chat,
                                    get_chat,
                                    rename_chat,
                                    delete_chat
                                    )

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AutoGraphRAG AI Buddy",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------

if "processed" not in st.session_state:
    st.session_state.processed = False

if "current_file" not in st.session_state:
    st.session_state.current_file = None

if "current_chat" not in st.session_state:

    chats = get_all_chats()

    if chats:
        st.session_state.current_chat = chats[0]["session_id"]

    else:
        chat = start_new_chat()
        st.session_state.current_chat = chat["session_id"]

# -----------------------------
# Header
# -----------------------------
st.title("Automotive AI Buddy")
st.caption("Upload any PDF and chat with it using Azure OpenAI + MongoDB RAG")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Automotive AI")
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
st.sidebar.subheader("Chats")

if st.sidebar.button("➕ New Chat"):

    chat = start_new_chat()

    st.session_state.current_chat = chat["session_id"]

    st.rerun()
for chat in get_all_chats():

    with st.sidebar.container(border=True):

        title = chat["title"]

        if chat["session_id"] == st.session_state.current_chat:
            title = "🟢 " + title

        if st.button(
            title,
            key=f"chat_{chat['session_id']}",
            use_container_width=True
        ):
            st.session_state.current_chat = chat["session_id"]
            st.rerun()

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "✏️ Rename",
                key=f"rename_{chat['session_id']}",
                use_container_width=True
            ):
                st.session_state.rename_chat = chat["session_id"]

        with col2:
            if st.button(
                "🗑 Delete",
                key=f"delete_{chat['session_id']}",
                use_container_width=True
            ):
                delete_chat(chat["session_id"])

                chats = get_all_chats()

                if chats:
                    st.session_state.current_chat = chats[0]["session_id"]
                else:
                    new_chat = start_new_chat()
                    st.session_state.current_chat = new_chat["session_id"]

                st.rerun()

if "rename_chat" in st.session_state:

    chat_id = st.session_state.rename_chat

    new_title = st.sidebar.text_input(
        "Rename Chat",
        key="rename_title"
    )

    if st.sidebar.button("Save Name"):

        rename_chat(chat_id, new_title)

        del st.session_state.rename_chat

        st.rerun()

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

    clear_chat(st.session_state.current_chat)
    st.rerun()

# -----------------------------
# Welcome Screen
# -----------------------------

messages = get_chat_history(st.session_state.current_chat)

if (
    len(messages) == 0
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
messages = get_chat_history(
    st.session_state.current_chat
)

for message in messages:

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
    add_user_message(
        st.session_state.current_chat,
        question
    )

    chat = get_chat(st.session_state.current_chat)

    if chat["title"] == "New Chat":

        rename_chat(
            st.session_state.current_chat,
            question[:40]
        )

    # Ask RAG
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = ask(question, selected_document)

            answer = result["answer"]
            sources = result["sources"]

        st.markdown(answer)

        shown = set()

        st.caption("📄 Sources")

        for source in sources:

            key = (
                source["document"],
                source["page"]
            )

            if key not in shown:

                shown.add(key)

                st.caption(
                    f"• {source['document']} - Page {source['page']}"
                )

    # Save assistant response
    add_assistant_message(
        st.session_state.current_chat,
        answer,
        sources
    )

    # Refresh page
    st.rerun()