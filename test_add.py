import add

def test_empty_str():
    assert add.Add('') == 0

def test_single_number():
    assert add.Add('1') == 1