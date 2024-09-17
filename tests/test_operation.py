from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(9,8)==17
    assert add(-1,1)==0
def test_sub():
    assert sub(10,5)==5
    assert sub(-2,1)==-1