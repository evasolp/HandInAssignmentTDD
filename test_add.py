import add
import pytest

def test_empty_str():
    assert add.Add('') == 0

def test_single_number():
    assert add.Add('1') == 1

def test_two_numbers():
    assert add.Add('1,2') == 3

def test_unknown_number_of_numbers():
    assert add.Add('10,2,5,22,1,1,68,43') == 152

def test_new_lines_delimiter():
    assert add.Add('1\n2,3') == 6

def test_ignore_numbers_over_1000():
    assert add.Add('1001,2') == 2

def test_negative_numbers() -> None:
    with pytest.raises(add.NegativeError):
        assert add.Add('2,-4,3,-5')

def test_different_delimiter():
    assert add.Add('//%\n1%2%3') == 6