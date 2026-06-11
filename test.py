class calc:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print(self.n1+self.n2) 
    def mul(self):
        print(self.n1*self.n2) 
    def sub(self):
        print(self.n1-self.n2) 
    def div(self):
        print(self.n1/self.n2) 

a=calc(15,15)
a.add()
a.sub()
a.div()
a.mul()