# Tech notes

Here are some tech notes.

## Installing

Download the source code from github: [maze_game](https://github.com/ortolanph/maze_game) 

## Requirements

Python 3.7 or higher.

## Configuring

Run the following command:

```shell
pip3 install -r requirements.txt
```

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

[Back](../README.md)