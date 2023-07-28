""" PyTest """
# import pytest

from src.vol01 import prob01
from src.vol01 import prob02
from src.vol01 import prob03

ANSWER = {
    'prob01': 233168,
    'prob02': 4613732,
    'prob03': 6857
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