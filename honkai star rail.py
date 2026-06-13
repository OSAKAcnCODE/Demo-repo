from abc import ABC,abstractmethod
class characters(ABC):

    def __init__(self,name):
        self.name=name
    @abstractmethod
    def health(self):
        pass
    @abstractmethod
    def basic(self):
        pass
    @abstractmethod
    def ult(self):
        pass
    @abstractmethod
    def skill(self):
        pass


class team(characters):

    def __init__(self,name):
        self.name=name
    def health(self):
        print(f'{self.name} has',5800)
    def skill(self):
        print(f'{self.name} used a skill')
    def basic(self):
        print(f'{self.name} used their basic attack')

    def ult(self):
        print(f'{self.name} user their ulimate attack')
       
  
jingliu=team("Jingliu")
jingliu.ult()
