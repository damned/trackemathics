import pytest
from trackemathics.value import Value

def test_value_can_tell_us_about_itself():
    assert Value(2).narrate() == 'i am 2. i am who i am.'

def test_value_can_tell_us_about_where_it_comes_from():
    assert Value(3, 'bob').narrate() == 'i am 3. from: bob'

class Bingo:
    def __init__(self, nickname):
        self.nickname = nickname

    def __repr__(self):
        return f"the bingo number, {self.nickname}"

def test_value_can_have_an_object_source():
    bingo_four = Value(4, Bingo('knock at the door'))
    assert bingo_four.narrate() == 'i am 4. from: the bingo number, knock at the door'

