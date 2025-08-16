from random import randint


class Die:
    def __init__(self, nb_of_faces: int = 6):
        self.nb_of_faces = nb_of_faces

    def throw(self, dies: int = 1) -> list[int]:
        return [randint(1, self.nb_of_faces) for _ in range(dies)]

    def throw_sum(self, dies: int = 2) -> int:
        return sum(self.throw(dies))
