import lib
import pytest
#тест сортировки пузырьком
class TestSortBubble:
    #задаем числа в порядке возрастания
    @pytest.fixture()
    def mintomaxnumbers(self):
        return [1,2,3,4,5,6,7,8,9,10]
    #задаем числа в случайном порядке
    @pytest.fixture()
    def numbers(self):
        return [38,18,0,1,4,71,3,4,9,2]
    #задаем одинаковые числа
    @pytest.fixture()
    def equalsnumbers(self):
        return [1,1,1,1,1,1,1,1,1,1]
    #задачем числа в порядке убывания
    @pytest.fixture()
    def maxtomin(self):
        return [10,9,8,7,6,5,4,3,2,1]
    #задачем числа с ошибкой, последний элемент типа str
    @pytest.fixture()
    def incorrectnumbers(self):
        return [1,2,3,4,5,6,7,8,9,'10']
    #тестируем сортировку с числами по возрастанию
    def testminmmaxnumbers(self,mintomaxnumbers):
        assert lib.sort(mintomaxnumbers) == [1,2,3,4,5,6,7,8,9,10]
    #тестируем сортировку с числами в случайном порядке
    def testnumbers(self,numbers):
        assert lib.sort(numbers) == [0,1,2,3,4,4,9,18,38,71]
    #тестируем сортировку с одинаковыми числами
    def testequalsnumbers(self,equalsnumbers):
        assert lib.sort(equalsnumbers) == [1,1,1,1,1,1,1,1,1,1]
    #тестируем сортировку с числами по убыванию
    def testmaxtomin(self,maxtomin):
        assert lib.sort(maxtomin) == [1,2,3,4,5,6,7,8,9,10]
    #тестируем сортировку с последним элементом массива типа str исключая ошибку
    def testincorrectnumberswithpytest(self,incorrectnumbers):
       with pytest.raises(TypeError):
           lib.sort(incorrectnumbers)
    #тестируем сортировку с последним элементом массива типа str
    def testincorrectnumber(self,incorrectnumbers):
        assert lib.sort(incorrectnumbers) == [1,2,3,4,5,6,7,8,9,10]

