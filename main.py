class calc:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2 

class add(calc):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)   
    def add(self):
        return self.n1+self.n2
class sub(calc):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)   
    def sub(self):
        return self.n1-self.n2
class mul(calc):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)   
    def mul(self):
        return self.n1*self.n2
class div(calc):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)   
    def div(self):
        return self.n1/self.n2
    
print(add(15,15))
mul(15,15)
sub(15,15)
div(15,15)