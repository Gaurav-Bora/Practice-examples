#oop
class PlayerCharacters:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def shout(self):
        print(f'my name is {self.name}')
    
    def run(self):
        print(f'i m running and my age is {self.age}')

player1 = PlayerCharacters('Gau', 24)
player2 = PlayerCharacters('Gaurav', 40)

print(player1.shout())        