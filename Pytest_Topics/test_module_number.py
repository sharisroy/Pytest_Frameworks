def test_addition_pass():
    assert 2 + 3 == 5


def test_addition_fail():
    assert 2 + 3 == 6, "failed test intentionally"


def test_truncating_division_pass():
    assert 5//3 == 1  # integer result
