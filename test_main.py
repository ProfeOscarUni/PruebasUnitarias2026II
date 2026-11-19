import pytest
from main import sum, es_mayor_que

def test_sum():
    assert sum(2, 3) == 5
    print("Test passed,")

def test_es_mayor_que():
    assert es_mayor_que(5, 3) == True
    assert es_mayor_que(3, 5) == False
    print("Test es_mayor_que passed,")
    
@pytest.mark.parametrize("input_x, input_y, expected", [
    (5, 3, 8),
    (-3, 5, 2),
    (-4, sum(4,2), 2),
])
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected
    print("Las funciones parametrizadas pasaron la prueba,")
    
if __name__ == "__main__":
    test_sum()
    test_es_mayor_que()
    test_sum_params()