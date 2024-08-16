def test_not_equal():
    assert 1 != 2


def test_bool_true():
    assert True
    assert 1


def test_bool_false():
    assert False, "Assertion False"


def test_character_match():
    assert "abc" == "abcd"


def test_multiple():
    assert 1 in divmod(9, 5)
    assert 'put' not in "this is pytest"
    assert [1, 2, 3] == [1, 2, 3]
