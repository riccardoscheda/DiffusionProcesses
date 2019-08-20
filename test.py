#####File for testing functions#####



import integration as int


from hypothesis import strategies as st
from hypothesis import given
from hypothesis.extra import numpy as enp
import numpy as np


@given(coord = st.tuples(st.floats(),st.floats()))
def test_phi(coord):
    """
    Tests
    if returns two float
    if the momenta is zero and if the coordinate q is different from zero
    """
    q , p = int.phi(coord[0],coord[1])

    assert isinstance(q, float)
    assert isinstance(p, float)
    #assert p == 0

@given(coord = st.tuples(st.floats(),st.floats(),st.floats(),st.floats(),st.floats()))
def test_euler(coord):
    """
    Tests
    if returns two float
    if the evolution of p is different from zero
    if the q is diferent from zero only if the momenta is different from zero
    """
    evoq, evop  = int.euler(coord[0],coord[1],abs(coord[2]),coord[3],coord[4])

    assert isinstance(evoq , float)
    assert isinstance(evop, float)

@given(coord = st.tuples(st.floats(),st.floats(),st.floats(),st.floats(),st.floats()))
def test_simplettic(coord):
    """
    Tests
    if returns two float
    if the evolution of p is different from zero
    if the q is diferent from zero only if the momenta is different from zero
    """
    evoq, evop  = int.simplettic(coord[0],coord[1],abs(coord[2]),coord[3],coord[4])

    assert isinstance(evoq , float)
    assert isinstance(evop, float)


@given(rho = enp.arrays(float,(1,10)))
def test_entropy(rho):
    assert isinstance(rho, np.ndarray)
    assert isinstance(int.entropy(rho), float)
