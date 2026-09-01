from rectangle import Rectangle

def test_valid_rectangle():
    box = Rectangle(5.0, 3.0)
    assert box.get_length() == 5.0
    assert box.get_width() == 3.0
    assert box.get_area() == 15.0

def test_negative_length():
    box = Rectangle(-4.0, 6.0)
    assert box.get_length() == 0.0
    assert box.get_width() == 6.0
    assert box.get_area() == 0.0

def test_negative_width():
    box = Rectangle(4.0, -6.0)
    assert box.get_length() == 4.0
    assert box.get_width() == 0.0
    assert box.get_area() == 0.0
