""" PyTest """
# import pytest

from src.vol01 import prob01
from src.vol01 import prob02
from src.vol01 import prob03

ANSWER = {
    'prob01': 233168,
    'prob02': 4613732,
    'prob03': 6857,
    'prob04': 906609,
    'prob05': 232792560,
    'prob06': 25164150,
}


def test_prob01():
    """ test prob01 """
    rst = prob01(top=1_000, div_list=[3, 5])

    assert rst == ANSWER['prob01']


def test_prob02():
    """ test prob02 """
    rst = prob02(top=4_000_000)

    assert rst == ANSWER['prob02']


def test_prob03():
    """ test prob03 """
    rst = prob03(tgt=600_851_475_143)

    assert rst == ANSWER['prob03']


def test_prob04():
    """ test prob04 """
    rst = prob04(num1_dig=3, num2_dig=3)

    assert rst == ANSWER['prob04']


def test_prob05():
    """ test prob05 """
    rst = prob05()

    assert rst == ANSWER['prob05']


def test_prob06():
    """ test prob06 """
    rst = prob06(tgt=100)

    assert rst == ANSWER['prob06']
