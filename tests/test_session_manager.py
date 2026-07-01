from src.memory.session_manager import (
    create_session,
    get_all_sessions,
    get_session
)

session = create_session("sample.pdf")

print(session)

print(get_session(session["session_id"]))

print(get_all_sessions())