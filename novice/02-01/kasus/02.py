def formalGreeting():
    print("How are you")
def casualGreeting():
    print("what's up")
    
def greet(type, greetFormal, greetCasual):
     if type == "formal":
         formalGreeting()
     elif type == "casual":
         casualGreeting()
        
greet("casual",formalGreeting, casualGreeting)