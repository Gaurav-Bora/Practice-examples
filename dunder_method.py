class Toy():
    def __init__(self,colour, age):
        self.colour = colour
        self.age = age
        self.mydict = {
            'name' : 'gaurav',
            'gender' : 'male'}
    def __str__(self):
        return f'{self.colour}'
    def __len__(self):
        return 10
    def __getitem__(self,i):
        return self.mydict(i)
action_fig = Toy('red', 0)
print(action_fig.__str__())
print(str(action_fig))
print(len(action_fig))
print(action_fig['name'])
        
    