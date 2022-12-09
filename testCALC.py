import lib
import pytest
#тест калькулятора
class TestCalc:
    #задаем числа и знак действия
    @pytest.fixture()
    def plus(self):
        return 10,10,'+'
    #задаем числа и знак действия
    @pytest.fixture()
    def minus(self):
        return 10,10,'-'
    #задаем числа и знак действия
    @pytest.fixture()
    def umnozhenie(self):
        return 10,10,'*'
    #задаем числа и знак действия
    @pytest.fixture()
    def delenie(self):
        return 10,10,'/'
    #задачем значения с ошибкой
    @pytest.fixture()
    def error(self):
        return '+','-','+'
    #тест калькулятора 10+10
    def testplus(self,plus):
        assert lib.calc(*plus) == 20
    #тест калькулятора 10-10
    def testminus(self,minus):
        assert lib.calc(*minus) == 0
    #тест калькулятора 10*10
    def testumnozhenine(self,umnozhenie):
        assert lib.calc(*umnozhenie) == 100
    #тест калькулятора 10/10
    def testdelenie(self,delenie):
        assert lib.calc(*delenie) == 1
    #тест калькулятора с ошибкой
    def testerror(self,error):
        assert lib.calc(error) == 0
    #тест калькулятора с ошибкой TypeError исключая ошибку
    def testerrorwithpytest(self,error):
        with pytest.raises(TypeError):
            lib.calc(error)

