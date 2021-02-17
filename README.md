# Maze Game

A simple game written in Python using the PyGame API.

## Release Notes

 * **2021-16-02**: First release
 * **2021-17-02**: Version with player interactive
 * **2021-17-02**: Integration with the [py_maze_api](https://github.com/ortolanph/py_maze_api) created by me
 * **2021-17-02**: Integration with console joysticks (PS4 and XBOX)

## Running

The maze is a 4 x 4 grid, just run the following command:

```shell
usage: mazegame [-h] [--width WIDTH] [--height HEIGHT]
                [--joy-profile {none,ps4,xbox,airflo}]
                [--print-maze PRINT_MAZE]

Creates a Maze Game session

optional arguments:
  -h, --help            show this help message and exit
  --width WIDTH         Width of the maze (min = 4 and max = 999)
  --height HEIGHT       Height of the maze (min = 4 and max = 999)
  --joy-profile {none,ps4,xbox,airflo}
                        Loads a Joystick Profile (ps4, xbox, airflo)
  --print-maze PRINT_MAZE
                        Prints the Maze

Be challenged!
```

Default values:

| Parameter | Default |
|:---------:|:-------:|
| `width` | `5` |
| `height` | `5` |
| `joy-profile` | `none` |
| `print-maze` | `False` |

## Installing Libs

Run the following command:

```shell
pip3 install -r requirements.txt
```

## Joysticks and buttons

The following Joysticks are supported:

 * PS4
 * XBOX
 * AirFlo (tests needed)

Desired Joysticks:

 * PS2
 * PS3
 * GameCube
 * SNES

### Keyboard Mapping

| Button | Action | Status |
|:------:|:------:|:------:|
| Arrows | Movement | Implemented |
| SPACE | Open Chests | In Development |
| A | Use Item | In Development |
| M | Minimap | In Development |
| S | Save Game | In Development |
| Q | Choose Item on the left | In Development |
| W | Choose Item on the right | In Development |
| P | Pause Game | In Development |

### PS4 Joystick

| Button | Action | Status |
|:------:|:------:|:------:|
| Arrows | Movement | Implemented |
| X | Open Chests | In Development |
| Circle | Use Item | In Development |
| Square | Minimap | In Development |
| Triangle | Save Game | In Development |
| L1 | Choose Item on the left | In Development |
| R1 | Choose Item on the right | In Development |
| OPTIONS | Pause Game | In Development |

### XBOX Joystick

| Button | Action | Status |
|:------:|:------:|:------:|
| Arrows | Movement | Implemented |
| A | Open Chests | In Development |
| B | Use Item | In Development |
| X | Minimap | In Development |
| Y | Save Game | In Development |
| L1 | Choose Item on the left | In Development |
| R1 | Choose Item on the right | In Development |
| START | Pause Game | In Development |

### AirFlo Joystick

| Button | Action | Status |
|:------:|:------:|:------:|
| Arrows | Movement | Implemented |
| 1 | Open Chests | In Development |
| 2 | Use Item | In Development |
| 3 | Minimap | In Development |
| 4 | Save Game | In Development |
| L1 | Choose Item on the left | In Development |
| R1 | Choose Item on the right | In Development |
| START | Pause Game | In Development |

## Next Steps

These are the next steps that will be taken:
 * Adding Treasures and Obstacles in the rooms
 * Adding images to Player, Walls, and Treasures
 * Adding a HUD
 * Skins to scenario
 * Player Characters
 * Player Profile and Game Save

Other Steps (not planned):
 * Customization using GUI
 * Auto save:
    * each 20 rooms visited
    * each maze completed
 * Statistics and Trophies:
    * Mazes Completed
    * Mazes Completed by dimension
    * Gold earned
    * Rooms visited
    * etc...
   