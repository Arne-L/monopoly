from random import randint

class Die:
    def __init__(self, nb_of_faces: int = 6):
        self.nb_of_faces = nb_of_faces

    def throw(self) -> int:
        return randint(1, self.nb_of_faces)
    
    def throw_multiple(self, dies: int = 2):
        return sum([self.throw() for _ in range(dies)])