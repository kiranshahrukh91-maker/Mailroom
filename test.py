from mailroom import count_daily_drinkers, count_group, count_subscribers, output_is_string, read_subscribers


def test_total_subscribers() -> None:
    # Output: what the function gives us
    text: str = read_subscribers()
    actual: int = count_subscribers(text)

    # Expected behaviour: what we want
    expected: int = 24

    assert actual == expected, "expected " + str(expected) + " subscribers, got " + str(actual)


def test_daily_drinkers() -> None:
    # Output: what the function gives us
    text: str = read_subscribers()
    actual: int = count_daily_drinkers(text)

    # Expected behaviour: what we want
    expected: int = 8

    assert actual == expected, "expected " + str(expected) + " daily-drinkers rows, got " + str(actual)


def test_tea_curious() -> None:
    # Output: what the function gives us
    text: str = read_subscribers()
    actual: int = count_group(text, "tea-curious")

    # Expected behaviour: what we want
    expected: int = 8

    assert actual == expected, "expected " + str(expected) + " tea-curious rows, got " + str(actual)


def test_gift_buyers() -> None:
    # Output: what the function gives us
    text: str = read_subscribers()
    actual: int = count_group(text, "gift-buyers")

    # Expected behaviour: what we want
    expected: int = 8

    assert actual == expected, "expected " + str(expected) + " gift-buyers rows, got " + str(actual)


def test_output_is_string() -> None:
    # Output: what the function gives us
    text: str = read_subscribers()
    actual: bool = output_is_string(text)

    # Expected behaviour: what we want
    expected: bool = True

    assert actual == expected, "read_subscribers() must return a str"


test_total_subscribers()
test_daily_drinkers()
test_tea_curious()
test_gift_buyers()
test_output_is_string()
print("All tests passed")
