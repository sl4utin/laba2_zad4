import pytest
import lib
#тест чисел Фибоначчи
class TestFebanachi:
    #тест чисел Фибоначчи с n = 10
    def testONcorrect(self):
        assert lib.fEbanachi(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    #тест чисел Фибоначчи c n = 0. Функция вызывает исключение IndexError.
    def testZEROcorrect(self):
        with pytest.raises(IndexError):
            lib.fEbanachi(0)
    #тест чисел Фибоначчи с n = 0
    def testZEROincorrect(self):
        assert lib.fEbanachi(0)
