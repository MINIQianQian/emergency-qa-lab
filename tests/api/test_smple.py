import pytest

from  src.emergency_qa_lab.emergency_service.sample import find_clockangle


@pytest.mark.parametrize("hours,mins,expected", [
    (3,0,90),
    (3,30,175),
    (6,0,180),
    (0,0,0)
])
def test_find_clockangle(hours,mins，expected):

    assert find_clockangle(hours,mins) == expected











