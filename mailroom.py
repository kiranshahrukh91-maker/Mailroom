# Mailroom functions: the code that does the work. The checks live in test.py.


def read_subscribers() -> str:
    file = open("Data/subscribers.csv")
    text: str = file.read()
    file.close()
    return text


def output_is_string(text: str) -> bool:
    return type(text) == str


def count_subscribers(text: str) -> int:
    lines: list[str] = text.splitlines()
    return len(lines) - 1  # the first line is the header, not a subscriber


def count_daily_drinkers(text: str) -> int:
    lines: list[str] = text.splitlines()
    count: int = 0
    for line in lines:
        if "daily-drinkers" in line:
            count += 1
    return count
