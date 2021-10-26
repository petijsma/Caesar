import pytest
from Casear_siphre import casear

def test_casear():
    text = 'aa'
    assert casear(text, 1) == 'bb'
    assert casear(text, -1) == 'zz'
    assert casear(text, 3) == 'dd'
    assert casear(text, -3) == 'xx'