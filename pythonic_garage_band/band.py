class Band():

    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self) -> str:
        return f"Hello, we are {self.name}"

    def __repr__(self) -> str:
        return f"{self.name} Members: {len(self.members)}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:

    instrument = ""
    title = ""

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self) -> str:
        return f"{self.title} instance. Name = {self.name}"
    
    def get_instrument(self):
        return self.instrument

class Guitarist(Musician):

    instrument = "guitar"
    title = "Guitarist"
    
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):

    instrument = "bass"
    title = "Bassist"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):

    instrument = "drums"
    title = "Drummer"

    def play_solo(self):
        return "rattle boom crash"