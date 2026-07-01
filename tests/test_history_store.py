from src.memory.session_manager import create_session
from src.memory.history_store import (
    save_message,
    load_messages,
    clear_history,
)

session = create_session("sample.pdf")

session_id = session["session_id"]

save_message(session_id, "user", "Hello")

save_message(session_id, "assistant", "Hi! How can I help you?")

messages = load_messages(session_id)

print(messages)

clear_history(session_id)

print(load_messages(session_id))