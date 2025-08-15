class Tile:
    def __init__(self, name: str):
        self.name = name

class Street(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Utility(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Railroad(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Card(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Go(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Jail(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class FreeParking(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class GoToJail(Tile):
    def __init__(self, name: str):
        super().__init__(name)
