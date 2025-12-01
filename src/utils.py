def format_lesson_text(data: dict) -> str:
    subject = data.get("subject", "")
    lesson_type = data.get("type", "")
    room = data.get("room", "")
    teacher = data.get("teacher", "")

    lines = []
    if subject:
        if lesson_type:
            lines.append(f"{subject} ({lesson_type})")
        else:
            lines.append(subject)
    if room:
        lines.append(f"aud. {room}")
    if teacher:
        lines.append(teacher)

    return "\n".join(lines)
