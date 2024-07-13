import json
import random
import re


class HexEffect:
    def __init__(self, duration="", sight="", earing="", ranged_attack="", flame="", flight="",
                 dc_concentration="", tiredness="", temporary_hp=""):

        self.duration = self.dynamic_duration(duration)
        self.sight = sight
        self.earing = earing
        self.ranged_attack = ranged_attack
        self.flame = flame
        self.flight = flight
        self.dc_concentration = dc_concentration
        self.tiredness = tiredness
        self.temporary_hp = temporary_hp

    @staticmethod
    def dynamic_duration(value):
        if value is not None:
            match1 = re.match(r"1d4", value)
            match2 = re.match(r"2d4", value)
            match3 = re.match(r"2d6", value)
            if match1:
                return random.randint(1, 4)
            elif match2:
                return random.randint(1, 4) + random.randint(1, 4)
            elif match3:
                return random.randint(1, 6) + random.randint(1, 6)
            else:
                return value

    def __repr__(self):
        return (f"HexEffect(duration={self.duration}, self.sight={self.sight}, self.earing={self.earing}, "
                f"self.ranged_attack={self.ranged_attack}, self.flame={self.flame}, self.flight={self.flight}, "
                f"self.dc_concentration={self.dc_concentration}, self.tiredness={self.tiredness}, "
                f"self.temporary_hp={self.temporary_hp})")


class Hex:
    def __init__(self, x, y, title, description, small_image_coords=None):
        self.x = x
        self.y = y
        self.title = title
        self.description = description
        self.effect = HexEffect()
        self.small_image_coords = small_image_coords or [0, 0]

    def __repr__(self):
        return (f"Hex({self.x}, {self.y}, {self.title}, {self.description}, "
                f"effect={self.effect, self.small_image_coords})")


class HexMemory:
    def __init__(self, max_memory=5):
        self.max_memory = max_memory
        self.memory = []

    def add_position(self, position):
        if len(self.memory) >= self.max_memory:
            self.memory.pop(0)
        self.memory.append(position)

    def get_previous_position(self):
        if self.memory:
            return self.memory[-1]
        return None

    def get_all_positions(self):
        return self.memory.copy()


class HexGrid:
    DIRECTIONS = {"N": (1, 0), "NE": (1, 1), "SE": (0, 1),
                  "S": (-1, 0), "SW": (-1, -1), "NW": (0, -1)}

    IMPOSSIBLE_MOVES = {((2, 0), "N"), ((1, -1), "N"), ((2, 1), "N")}

    LOOPS = {
        "WEST": {((0, -2), "SW"): (-1, -2), ((-2, -2), "NW"): (-1, -2)},
        "EAST": {((2, 2), "SE"): (1, 2), ((0, 2), "NE"): (1, 2)},
        "SOUTH_WEST": {((-2, 0), "SW"): (-2, -1)},
        "SOUTH_EAST": {((-2, 0), "SE"): (-1, 1)}
    }

    def __init__(self, init_file=None, current_position=(1, 0)):
        self.min_coord = -2
        self.max_coord = 2
        self.hex_memory = HexMemory()
        self.grid = self.init_grid(init_file)
        self.current_position = current_position

    @staticmethod
    def init_grid(init_file=None):
        grid = {}
        if init_file is not None:
            with open(init_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    x, y = eval(key)
                    title = value["title"]
                    description = value["description"]
                    small_image_coords = value.get("small_image_coords", [0, 0])
                    effect = HexEffect(
                        duration=value.get("duration", ""),
                        sight=value.get("sight", ""),
                        earing=value.get("earing", ""),
                        ranged_attack=value.get("ranged_attack", ""),
                        flame=value.get("flame", ""),
                        flight=value.get("flight", ""),
                        dc_concentration=value.get("dc_concentration", ""),
                        tiredness=value.get("tiredness", ""),
                        temporary_hp=value.get("temporary_hp", "")
                    )
                    hex_tile = Hex(x, y, title, description, small_image_coords)
                    hex_tile.effect = effect
                    grid[(x, y)] = hex_tile
        else:
            print("error, no file given")
        return grid

    def get_hex(self, coordinates):
        return self.grid.get(coordinates, None)

    def move(self, coordinates, direction_name):
        if (coordinates, direction_name) in self.IMPOSSIBLE_MOVES:
            return coordinates

        for loop_key, loop_moves in self.LOOPS.items():
            if (coordinates, direction_name) in loop_moves:
                return loop_moves[(coordinates, direction_name)]

        direction = self.DIRECTIONS[direction_name]
        new_coordinates = [
            coordinates[0] + direction[0],
            coordinates[1] + direction[1],
        ]
        x, y = new_coordinates

        if (direction_name in ("N", "S") and
                (x < self.min_coord or x > self.max_coord or
                 (y - x) < self.min_coord or (y - x) > self.max_coord)):
            new_coordinates = [coordinates[1] - coordinates[0], coordinates[1]]

        if (direction_name in ("NW", "SW", "NE", "SE") and
                (x < self.min_coord or x > self.max_coord or
                 y < self.min_coord or y > self.max_coord or
                 (y - x) < self.min_coord or (y - x) > self.max_coord)):
            if direction_name in ("NW", "SE"):
                new_coordinates = [coordinates[0], -(coordinates[1] - coordinates[0])]
            else:
                new_coordinates = [-coordinates[1], -coordinates[0]]
        return tuple(new_coordinates)

    def move_current_position(self, direction_name):
        self.hex_memory.add_position(self.current_position)
        self.current_position = self.move(self.current_position, direction_name)
        return self.current_position

    def move_previous_position(self):
        previous_position = self.hex_memory.get_previous_position()
        if previous_position:
            self.current_position = previous_position
            self.hex_memory.memory.pop()
        return self.current_position

def random_move():
    probability = random.uniform(0, 100)

    if probability <= 6:
        return "N"
    elif probability <= 17:
        return "NW"
    elif probability <= 28:
        return "NE"
    elif probability <= 49:
        return "SW"
    elif probability <= 70:
        return "SE"
    else:
        return "S"


def main():
    print("*****-- TEST DE METEO --******")
    print(random_move())
    new_hex_grid = HexGrid(init_file="weather_flower.json")
    print(f"Current position : {new_hex_grid.current_position}\n")
    question = ""
    while question not in ("N", "n"):
        question = input("Keep moving ? (Y/N) ")
        randomx = random_move()
        new_position = new_hex_grid.move_current_position(randomx)
        print(f"Direction : {randomx}")
        print(f"Current position : {new_position}")
        print(f"Memory : {new_hex_grid.hex_memory.get_all_positions()}")

    print("-------------")
    print(f"Memory : {new_hex_grid.hex_memory.get_all_positions()}")
    question2 = ""
    while question2 not in ("N", "n"):
        question2 = input("go back ? (Y/N) ")
        new_position = new_hex_grid.move_previous_position()
        print(f"Current position : {new_position}")
        print(f"Memory : {new_hex_grid.hex_memory.get_all_positions()}")



if __name__ == "__main__":
    main()
