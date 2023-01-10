def is_message_valid(message: dict ) -> bool:
    if isinstance(message, dict) and message.get("type") is not None:
        return True
    return False
