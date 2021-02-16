CORNERS = [
    [0, 0, 50, 50],
    [750, 0, 50, 50],
    [750, 750, 50, 50],
    [0, 750, 50, 50]
]

NORTH_EXIT = [
    [50, 0, 250, 50],
    [500, 0, 250, 50]
]

NORTH_WALL = [
    [50, 0, 700, 50]
]

EAST_EXIT = [
    [750, 50, 50, 250],
    [750, 500, 50, 250]
]

EAST_WALL = [
    [750, 50, 50, 700]
]

SOUTH_EXIT = [
    [50, 750, 250, 50],
    [500, 750, 250, 50]
]

SOUTH_WALL = [
    [50, 750, 700, 50]
]

WEST_EXIT = [
    [0, 50, 50, 250],
    [0, 500, 50, 250]
]

WEST_WALL = [
    [0, 50, 50, 700]
]

ROOM_ITEMS = {
    1: {"exit": NORTH_EXIT, "wall": NORTH_WALL},
    2: {"exit": EAST_EXIT, "wall": EAST_WALL},
    3: {"exit": SOUTH_EXIT, "wall": SOUTH_WALL},
    4: {"exit": WEST_EXIT, "wall": WEST_WALL}
}
