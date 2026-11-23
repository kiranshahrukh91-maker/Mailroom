# Mailroom functions: the code that does the work. The checks live in test.py.
import sys


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


def count_group(text: str, group: str) -> int:
    lines: list[str] = text.splitlines()
    count: int = 0
    for line in lines:
        if group in line:
            count += 1
    return count


if __name__ == "__main__":
    word: str = sys.argv[1]
    if word == "subscribers":
        text: str = read_subscribers()
        print("Total subscribers:", count_subscribers(text))
        print("Daily drinkers:", count_daily_drinkers(text))
        print("Tea curious:", count_group(text, "tea-curious"))
        print("Gift buyers:", count_group(text, "gift-buyers"))
