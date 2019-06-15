import pytest
from trackemathics.value import Value

def test_value_can_tell_us_about_itself():
    assert Value(2).narrate() == 'i am 2. i am who i am.'

def test_value_can_tell_us_about_where_it_comes_from():
    assert Value(3, 'bob').narrate() == 'i am 3. from: bob'

def test_value_can_have_an_object_source():
    bingo_four = Value(4, BingoSource('knock at the door'))
    assert bingo_four.narrate() == 'i am 4. from: the bingo number, knock at the door'

def test_the_result_of_an_addition_can_narrate_where_it_comes_from():
    three = Value(3, BingoSource('cup of tea'))
    eight = Value(8, BingoSource('garden gate'))

    eleven = three + eight
    assert eleven.value == 11
    assert eleven.narrate() == '''i am 11. from: 3 + 8
where:
i am 3. from: the bingo number, cup of tea
i am 8. from: the bingo number, garden gate''' 


class BingoSource:
    def __init__(self, nickname):
        self.nickname = nickname

    def __repr__(self):
        return f"the bingo number, {self.nickname}"

