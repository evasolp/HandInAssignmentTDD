import add

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

