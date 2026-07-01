from src.memory.chat_history import *

chat = start_new_chat("sample.pdf")

session_id = chat["session_id"]

add_user_message(session_id, "Who is the author?")

add_assistant_message(session_id, "The author is John Doe.")

print(get_chat_history(session_id))

print(get_all_chats())