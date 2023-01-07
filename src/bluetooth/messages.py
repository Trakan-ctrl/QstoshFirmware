def is_message_valid(message: dict | None) -> bool:
    if isinstance(message, dict) and message.get("type") is not None:
        return True
    return False
