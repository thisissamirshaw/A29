#WAP to create a qsp 
from abc import ABC,abstractmethod
class qsp(ABC):
    @abstractmethod
    def ch1():
        pass
    @abstractmethod
    def ch2():
        pass

class pyspider(qsp):
    def ch1():
        print('Kartik')
    def ch2():
        print('Samir')    

ob=pyspider()
print(pyspider.ch1())            