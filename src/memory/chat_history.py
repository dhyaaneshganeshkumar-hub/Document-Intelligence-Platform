from src.memory.session_manager import (
    create_session,
    get_all_sessions,
    get_session,
    delete_session,
    rename_session
)

from src.memory.history_store import (
    save_message,
    load_messages,
    clear_history
)


def start_new_chat(document_name="General"):
    return create_session(document_name)


def get_chat(session_id):
    return get_session(session_id)


def get_chat_history(session_id):
    return load_messages(session_id)


def add_user_message(session_id, message):
    return save_message(session_id, "user", message)


def add_assistant_message(session_id, message, sources=None):
    return save_message(session_id, "assistant", message, sources)


def get_all_chats():
    return get_all_sessions()


def delete_chat(session_id):
    return delete_session(session_id)


def clear_chat(session_id):
    return clear_history(session_id)


def rename_chat(session_id, title):
    return rename_session(session_id, title)