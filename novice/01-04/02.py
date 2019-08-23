class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        self.name = name
        self.legs = legs
        self.hibernate = hibernate
class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        Animal.__init__(self,name,legs)
        self.hibernate = hibernate
        
yogi = Bear('Yogi')
print(yogi.name)
print(yogi.legs)
print(yogi.hibernate)