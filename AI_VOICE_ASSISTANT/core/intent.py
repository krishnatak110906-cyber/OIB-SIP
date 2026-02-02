def detect_intent(text):
    text = text.lower()

    if "weather" in text:
        return "weather"
    elif "time" in text:
        return "time"
    elif "send email" in text or "email" in text:
        return "email"
    elif "remind" in text:
        return "reminder"
    elif "turn on" in text or "turn off" in text or "smart home" in text:
        return "smarthome"
    elif "hello" in text or "hi" in text or "greet" in text:
        return "greet"
    else:
        return "unknown"
