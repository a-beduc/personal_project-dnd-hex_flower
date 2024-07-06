directions = {"N": (1, 0, -1), "NE": (1, 1, 0), "SE": (0, 1, 1), "S": (-1, 0, 1), "SW": (-1, -1, 0), "NW": (0, -1, -1)}


def move(coordinates, direction_name):
    direction = directions[direction_name]
    new_coordinates = [coordinates[0] + direction[0], coordinates[1] + direction[1], coordinates[2] + direction[2]]
    x, y, z = new_coordinates

    if direction_name in ("N", "S") and (x < -2 or x > 2 or z < -2 or z > 2):
        new_coordinates = [-coordinates[0], coordinates[1], -coordinates[2]]

    if direction_name in ("NW", "SW", "NE", "SE") and (x < -2 or x > 2 or y < -2 or y > 2 or z < -2 or z > 2):
        if direction_name in ("NW", "SE"):
            new_coordinates = [coordinates[0], -coordinates[2], -coordinates[1]]
        else:
            new_coordinates = [-coordinates[1], -coordinates[0], coordinates[2]]

    return tuple(new_coordinates)


def main():
    current_coordinates = (0, 0, 0)
    print("Mouvement du nord au Sud")
    print(current_coordinates)
    current_coordinates = move(current_coordinates, "N")
    print(current_coordinates)
    current_coordinates = move(current_coordinates, "N")
    print(current_coordinates)
    current_coordinates = move(current_coordinates, "N")
    print(current_coordinates)
    current_coordinates = move(current_coordinates, "N")
    print(current_coordinates)
    current_coordinates = move(current_coordinates, "N")
    print(current_coordinates)

    print("-------")
    print("Mouvement du nord au Sud")
    current_coordinates2 = (0, 0, 0)
    current_coordinates2 = move(current_coordinates2, "NE")
    print(current_coordinates2)
    current_coordinates2 = move(current_coordinates2, "NE")
    print(current_coordinates2)
    current_coordinates2 = move(current_coordinates2, "NE")
    print(current_coordinates2)
    current_coordinates2 = move(current_coordinates2, "NE")
    print(current_coordinates2)
    current_coordinates2 = move(current_coordinates2, "NE")
    print(current_coordinates2)

if __name__ == '__main__':
    main()

