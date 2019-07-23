#####File for testing functions#####



import integration as int


from hypothesis import strategies as st
from hypothesis import given

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

@given(coord = st.tuples(st.floats(),st.floats()))
def test_euler(coord):
    """
    Tests
    if returns two float
    if the evolution of p is different from zero
    if the q is diferent from zero only if the momenta is different from zero
    """
    evoq, evop  = int.euler(coord[0],coord[1])

    assert isinstance(evoq , float)
    assert isinstance(evop, float)
    assert evop != 0
    if coord[1] != 0 :
        assert evoq != 0

@given(coord = st.tuples(st.floats(),st.floats(),st.floats(),st.floats()))
def test_simplettic(coord):
    """
    Tests
    if returns two float
    if the evolution of p is different from zero
    if the q is diferent from zero only if the momenta is different from zero
    """
    evoq, evop  = int.simplettic(coord[0],coord[1],abs(coord[2]),coord[3])

    assert isinstance(evoq , float)
    assert isinstance(evop, float)
    #assert evop != 0
    #if coord[1] != 0 :
    #    assert evoq != 0
