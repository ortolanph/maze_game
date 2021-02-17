# Maze Game

A simple game written in Python using the PyGame API.

## Release Notes

 * **2021-16-02**: First release
 * **2021-17-02**: Version with player interactive
 * **2021-17-02**: Integration with the [py_maze_api](https://github.com/ortolanph/py_maze_api) created by me 

## Running

The maze is a 4 x 4 grid, just run the following command:

```shell
python main.py [-h] [--width 0-999] [--height 0-999] [--print-maze True]
```

Where:
 * **(Optional)** `--width` is the width between 4 and 999 
 * **(Optional)** `--height` is the width between 4 and 999
 * **(Optional)** `--print-maze` prints the maze

This is the help:

```shell
usage: mazegame [-h] [--width WIDTH] [--height HEIGHT]
                [--print-maze PRINT_MAZE]

Creates a Maze Game session

optional arguments:
  -h, --help            show this help message and exit
  --width WIDTH         Width of the maze (min = 4 and max = 999)
  --height HEIGHT       Height of the maze (min = 4 and max = 999)
  --print-maze PRINT_MAZE
                        Prints the Maze

Be challenged!
```

For now that's not needed to inform any parameter.

## Installing Libs

Run the following command:

```shell
pip3 install -r requirements.txt
```

## Next Steps

These are the next steps that will be taken:
 
 * Integration with console joysticks (PS4 and XBOX)
 * Adding Treasures and Obstacles in the rooms
 * Adding images to Player, Walls, and Treasures
 * Adding a HUD