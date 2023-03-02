from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "JS"
    expected_count = 148

    result = count_ocurrences(path, word)

    assert result == expected_count
