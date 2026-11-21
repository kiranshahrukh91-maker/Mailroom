# Mailroom, step 1: a tiny inbox held in a list of dictionaries.
# Uses only Chapter 13 lessons 13.1 to 13.7.

emails: list[dict[str, str]] = [
    {"sender": "ali@example.com", "subject": "Invoice 204 is overdue", "priority": "high"},
    {"sender": "news@shop.example", "subject": "Weekly deals", "priority": "low"},
    {"sender": "sara@example.com", "subject": "Lunch on Friday?", "priority": "normal"},
]


def is_urgent(email: dict[str, str]) -> bool:
    return email["priority"] == "high"


urgent_subjects: list[str] = [e["subject"] for e in emails if is_urgent(e)]

print("Total emails:", len(emails))
print("Urgent subjects:", urgent_subjects)
