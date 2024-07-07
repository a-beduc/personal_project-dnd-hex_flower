import json


class Hex:
    def __init__(self, x, y, z, title, description, effect=None):
        self.x = x
        self.y = y
        self.z = z
        self.title = title
        self.description = description
        self.effect = effect

    def __repr__(self):
        return f"Hex({self.x}, {self.y}, {self.z}, self.{self.title}, {self.description}, {self.effect})"


class HexGrid:
    DIRECTIONS = {"N": (1, 0, -1), "NE": (1, 1, 0), "SE": (0, 1, 1),
                  "S": (-1, 0, 1), "SW": (-1, -1, 0), "NW": (0, -1, -1)}

    IMPOSSIBLE_MOVES = {((2, 0, -2), "N"), ((1, -1, -2), "N"), ((2, 1, -1), "N")}

    LOOPS = {
        "WEST": {((0, -2, -2), "SW"): (-1, -2, -1), ((-2, -2, 0), "NW"): (-1, -2, -1)},
        "EAST": {((2, 2, 0), "SE"): (1, 2, 1), ((0, 2, 2), "NE"): (1, 2, 1)},
        "SOUTH_WEST": {((-2, 0, 2), "SW"): (-2, -1, 1)},
        "SOUTH_EAST": {((-2, 0, 2), "SE"): (-1, 1, 2)}
    }

    def __init__(self, init_file=None, current_position=(1, 0, -1)):
        self.min_coord = -2
        self.max_coord = 2
        self.grid = self.init_grid(init_file)
        self.current_position = current_position

    @staticmethod
    def init_grid(init_file=None):
        grid = {}
        if init_file is not None:
            with open(init_file, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    x, y, z = eval(key)
                    title = value["title"]
                    description = value["description"]
                    effect = value["effect"]
                    grid[(x, y, z)] = Hex(x, y, z, title, description, effect)
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
            coordinates[2] + direction[2]
        ]
        x, y, z = new_coordinates

        if (direction_name in ("N", "S") and
                (x < self.min_coord or x > self.max_coord or
                 z < self.min_coord or z > self.max_coord)):
            new_coordinates = [-coordinates[0], coordinates[1], -coordinates[2]]

        if (direction_name in ("NW", "SW", "NE", "SE") and
                (x < self.min_coord or x > self.max_coord or
                 y < self.min_coord or y > self.max_coord or
                 z < self.min_coord or z > self.max_coord)):
            if direction_name in ("NW", "SE"):
                new_coordinates = [coordinates[0], -coordinates[2], -coordinates[1]]
            else:
                new_coordinates = [-coordinates[1], -coordinates[0], coordinates[2]]
        return tuple(new_coordinates)

    def move_current_position(self, direction_name):
        self.current_position = self.move(self.current_position, direction_name)
        return self.current_position


def main():
    print("*****-- LOOP EAST 1 --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(2, 2, 0))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("SE")
    print(f"Current position : {new_position}\n")

    print("*****-- LOOP EAST 2 --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(0, 2, 2))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("NE")
    print(f"Current position : {new_position}\n")

    print("*****-- LOOP WEST 1 --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(0, -2, -2))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("SW")
    print(f"Current position : {new_position}\n")

    print("*****-- LOOP WEST 2 --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(-2, -2, 0))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("NW")
    print(f"Current position : {new_position}\n")

    print("*****-- LOOP SOUTH EAST --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(-2, 0, 2))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("SE")
    print(f"Current position : {new_position}\n")

    print("*****-- LOOP SOUTH WEST --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(-2, 0, 2))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("SW")
    print(f"Current position : {new_position}\n")

    print("*****-- STOP NORTH WEST --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(1, -1, -2))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("N")
    print(f"Current position : {new_position}\n")

    print("*****-- STOP NORTH EAST --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(2, 1, -1))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("N")
    print(f"Current position : {new_position}\n")

    print("*****-- STOP NORTH NORTH --******")
    new_hex_grid = HexGrid(init_file="weather_flower.json", current_position=(2, 0, -2))
    print(f"Current position : {new_hex_grid.current_position}")
    new_position = new_hex_grid.move_current_position("N")
    print(f"Current position : {new_position}\n")


if __name__ == "__main__":
    main()
