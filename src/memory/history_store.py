import json
from pathlib import Path
from datetime import datetime

from src.memory.session_manager import get_session

CHAT_HISTORY_DIR = Path("data/chat_history")


def get_session_path(session_id):
    return CHAT_HISTORY_DIR / f"{session_id}.json"


def load_messages(session_id):
    """
    Returns all messages in a session.
    """
    session = get_session(session_id)

    if session is None:
        return []

    return session["messages"]


def save_message(session_id, role, content, sources=None):
    """
    Appends a new message to an existing session.
    """

    session = get_session(session_id)

    if session is None:
        return False

    session["messages"].append(
        {
            "role": role,
            "content": content,
            "sources": sources or []
        }
    )

    session["updated_at"] = datetime.now().isoformat()

    with open(get_session_path(session_id), "w") as f:
        json.dump(session, f, indent=4)

    return True


def clear_history(session_id):
    """
    Clears all messages but keeps the session.
    """

    session = get_session(session_id)

    if session is None:
        return False

    session["messages"] = []

    session["updated_at"] = datetime.now().isoformat()

    with open(get_session_path(session_id), "w") as f:
        json.dump(session, f, indent=4)

    return True
