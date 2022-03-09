


class Band:
    
    list = []

    def __init__(self,name,members):
        self.name = name
        self.members = members
        
        Band.list += [self]

    def __str__(self):
        return f'Band name : {self.name}'
    
    def __repr__(self):
        return f'Name = {self.name}'

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.list





class Musician:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'{self.get_instance()} instance. Name = {self.name}'

    def get_instrument(self):
        return "instrument"
    
    def get_instance(self):
        return "instance"

    def play_solo(self):
        return "play_solo"




class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"
    
    def get_instance(self):
        return "Guitarist"

    def play_solo(self):
        return "face melting guitar solo"
        

# Jan = Guitarist("Jan")
# print(Jan)
# print(repr(Jan))


class Bassist(Musician):
    def get_instrument(self):
        return "bass"
    
    def get_instance(self):
        return "Bassist"

    def play_solo(self):
        return "rattle boom crash"
    

class Drummer(Musician):
    def get_instrument(self):
        return "drums"
    
    def get_instance(self):
        return "Drummer"

    def play_solo(self):
        return "bom bom buh bom"

# Band1 = Band("XYZ",[Guitarist("Jan"),Bassist("mohi"),Drummer("Ahmad")])
# print(Band1.play_solos())
# print(Band1.to_list())
