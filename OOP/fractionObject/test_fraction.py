import pytest
from fraction import Fraction

    
def test_initialization():
    """Test fraction creation"""
    f = Fraction(5,8) 
    assert f.__str__() == "5/8"
    assert f.as_decimal == 0.625
    with pytest.raises(ZeroDivisionError):
        f2 = Fraction(1,0)

def test_add():
    """Test the addition function"""
    f1 = Fraction(5,8) 
    f2 = Fraction(5,8) 

    add_them_up = f1 + f2
    assert add_them_up.__str__() != "10/8" 
    assert add_them_up.__str__() != "5/4" 
    assert add_them_up.__str__() == "1-1/4" 
    assert add_them_up.as_decimal == 1.25

    f3 = Fraction(8, 19)
    f4 = Fraction(7, 13)

    fracSum = f3 + f4
    assert fracSum.__str__() == "237/247"
    assert fracSum.as_decimal == 0.960
  
def test_subtract():
    """Test the addition function"""
    f1 = Fraction(1,2) 
    f2 = Fraction(2,1) 
    f3 = Fraction(21, 25)
    f4 = Fraction(32, 21)
    total = f1 / f2
    assert total.__str__() == "1/4" 
    assert total.as_decimal == 0.25
    difference = f3 - f4
    assert difference.__str__() == "-359/525"
    assert difference.as_decimal == -0.684


def test_multiply():
    """ """
    f1 = Fraction(5,8) 
    f2 = Fraction(2,1)
    f3 = f1 * f2
    f4 = Fraction(0, 1) * Fraction(1, 4)
    assert f3.__str__() != "10/8"
    assert f3.__str__() != "5/4"
    assert f3.as_decimal == 1.25
    assert f4.__str__() == "0"

def test_divide():
    """ """
    f1 = Fraction(5,8) 
    f2 = Fraction(1,1)
    f3 = f1 / f2
    f4 = Fraction(1,4)
    f5 = Fraction(0,1)
    assert f3.__str__() == "5/8"
    assert f3.as_decimal == 0.625
    with pytest.raises(ZeroDivisionError):
        f4/f5

def test_comparisons():
    """ """
    f1 = Fraction(12,15) 
    f2 = Fraction(10,16)
    assert f1 > f2
    assert f2 < f1