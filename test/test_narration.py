import pytest
from trackemathics.value import Value

def test_value_can_tell_us_about_itself():
    assert Value(2).narrate() == 'i am 2. i am who i am.'

def test_value_can_tell_us_about_where_it_comes_from():
    assert Value(3, 'bob').narrate() == 'i am 3. from: bob'