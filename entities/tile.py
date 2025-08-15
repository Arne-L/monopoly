class Tile:
    def __init__(self, name: str):
        self.name = name


class BuyableTile(Tile):
    def __init__(self, name: str, land_value: int, mortgage_value: int, owner_id: int | None = None):
        super().__init__(name)
        self.owner_id = owner_id
        self.is_mortgaged = False
        self.land_value = land_value
        self.mortgage_value = mortgage_value

    def get_current_value(self):
        if self.is_mortgaged:
            return self.mortgage_value
        else:
            return self.land_value


class Street(BuyableTile):
    def __init__(
        self,
        name: str,
        color: str,
        land_value: int,
        base_rent: int,
        single_home_rent: int,
        double_home_rent: int,
        triple_home_rent: int,
        quadruple_home_rent: int,
        hotel_rent: int,
        home_cost: int,
        hotel_cost: int,
        mortgage_value: int,
    ):
        super().__init__(name, land_value=land_value, mortgage_value=mortgage_value)
        self.color = color
        self.base_rent = base_rent
        self.single_home_rent = single_home_rent
        self.double_home_rent = double_home_rent
        self.triple_home_rent = triple_home_rent
        self.quadruple_home_rent = quadruple_home_rent
        self.hotel_rent = hotel_rent
        self.home_cost = home_cost
        self.hotel_cost = hotel_cost
        self.nb_of_homes = 0
        self.nb_of_hotels = 0

    def get_current_value(self):
        if self.is_mortgaged:
            return self.mortgage_value
        else:
            return self.land_value + self.home_cost * self.nb_of_homes + self.hotel_cost * self.nb_of_hotels


class Utility(BuyableTile):
    def __init__(self, name: str, land_value: int, mortgage_value: int):
        super().__init__(name, land_value=land_value, mortgage_value=mortgage_value)


class Railroad(BuyableTile):
    def __init__(self, name: str, land_value: int, mortgage_value: int):
        super().__init__(name, land_value=land_value, mortgage_value=mortgage_value)


class CardTile(Tile):
    def __init__(self, name: str, card_type: str):
        super().__init__(name)
        self.card_type = card_type


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
