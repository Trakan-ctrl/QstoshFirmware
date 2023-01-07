def is_message_valid(message: dict) -> bool:
    if not message:
        return False
    if isinstance(message, dict) and message["topic"] is not None:
        return True
