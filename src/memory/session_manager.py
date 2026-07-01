import json
import uuid
from pathlib import Path
from datetime import datetime

CHAT_HISTORY_DIR = Path("data/chat_history")
CHAT_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
def create_session(document_name="General"):
    session_id = str(uuid.uuid4())

    session = {
        "session_id": session_id,
        "title": "New Chat",
        "document": document_name,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "messages": []
    }

    file_path = CHAT_HISTORY_DIR / f"{session_id}.json"

    with open(file_path, "w") as f:
        json.dump(session, f, indent=4)

    return session
def get_session(session_id):
    file_path = CHAT_HISTORY_DIR / f"{session_id}.json"

    if not file_path.exists():
        return None

    with open(file_path, "r") as f:
        return json.load(f)
def get_all_sessions():
    sessions = []

    for file in CHAT_HISTORY_DIR.glob("*.json"):
        with open(file, "r") as f:
            sessions.append(json.load(f))

    sessions.sort(
        key=lambda x: x["updated_at"],
        reverse=True
    )

    return sessions
def delete_session(session_id):
    file_path = CHAT_HISTORY_DIR / f"{session_id}.json"

    if file_path.exists():
        file_path.unlink()
def rename_session(session_id, title):
    session = get_session(session_id)

    if session is None:
        return

    session["title"] = title
    session["updated_at"] = datetime.now().isoformat()

    file_path = CHAT_HISTORY_DIR / f"{session_id}.json"

    with open(file_path, "w") as f:
        json.dump(session, f, indent=4)