class user():
    def sign_in(self):
        print('logged in')
class wizard(user):
    def __init__(self,name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attck with power of {self.power}')
    
class Archer(user):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    def check_arrows(self):
        print(f'{self.arrows} remaining')
        def run(self):
            print('ran very fast')
class Liger(wizard,Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        wizard.__init__(self, name, power)
        
Liger1 = Liger('gaurav', 50, 40)
print(Liger1.arrows)
print(Liger1.power)
print(Liger1.sign_in())
    
        
        
    