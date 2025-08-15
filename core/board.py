import json
from entities.tile import Street, Utility, Railroad, CardTile, Go, Jail, FreeParking, GoToJail, Tile, BuyableTile

class Board:
    def __init__(self):
        self.tiles: list[Tile] = []
        self._load_tiles()

    def get_tile_at(self, index: int) -> Tile:
        assert 0 <= index < len(self.tiles), f"The given tile index {index} falls outside the board ranging from 0 to {len(self.tiles) - 1}"
        return self.tiles[index]
    
    def get_tiles_of(self, player_id: int) -> list[BuyableTile]:
        return [tile for tile in self.tiles if isinstance(tile, BuyableTile) and tile.owner_id == player_id]
    
    def __len__(self):
        return len(self.tiles)

    def _load_tiles(self):
        with open("board.json", "r") as file:
            board_data = json.load(file)

            # TODO: Still need to check that every tile has the name, position and type key
            sorted_board_data = sorted(board_data, key=lambda tile: tile["position"])

            for tile in sorted_board_data:
                assert tile["type"] is not None, "A tile in the board data file does not have the type key, which is required for each tile."
                assert len(self.tiles) == tile["position"], f"The tile {tile["name"]} has position {tile["position"]} while it is expected to be at {len(self.tiles)}."

                if tile["type"] == "street":
                    self.tiles.append(Street(name=tile["name"],
                                              color=tile["color"], 
                                              land_value=tile["land_value"], 
                                              base_rent=tile["base_rent"], 
                                              single_home_rent=tile["single_home_rent"], 
                                              double_home_rent=tile["double_home_rent"], 
                                              triple_home_rent=tile["triple_home_rent"], 
                                              quadruple_home_rent=tile["quadruple_home_rent"], 
                                              hotel_rent=tile["hotel_rent"], 
                                              home_cost=tile["home_cost"], 
                                              hotel_cost=tile["hotel_cost"], 
                                              mortgage_value=tile["mortgage_value"]))
                elif tile["type"] == "utility":
                    self.tiles.append(Utility(name=tile["name"], land_value=tile["land_value"], mortgage_value=tile["mortgage_value"]))
                elif tile["type"] == "railroad":
                    self.tiles.append(Railroad(name=tile["name"], land_value=tile["land_value"], mortgage_value=tile["mortgage_value"]))
                elif tile["type"] == "card":
                    self.tiles.append(CardTile(name=tile["name"], card_type=tile["card_type"]))
                elif tile["type"] == "go":
                    self.tiles.append(Go(name=tile["name"]))
                elif tile["type"] == "jail":
                    self.tiles.append(Jail(name=tile["name"]))
                elif tile["type"] == "free parking":
                    self.tiles.append(FreeParking(name=tile["name"]))
                elif tile["type"] == "go to jail":
                    self.tiles.append(GoToJail(name=tile["name"]))
                else:
                    raise ValueError(f"Unknown tile type: {tile['type']} for tile {tile['name']} at position {tile['position']}")