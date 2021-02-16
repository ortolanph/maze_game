# -*- coding: utf-8 -*-
import sys

import pygame

from ColorPallete import BASE_PALLETE
from GameRoom import GameRoom

BLACK = (0, 0, 0)
arguments = sys.argv[1:]


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 800])

    # Set the title of the window
    pygame.display.set_caption('Maze')

    maze = [
        [
            GameRoom([2, 3], "NORMAL"),
            GameRoom([4], "START"),
            GameRoom([2], "NORMAL"),
            GameRoom([3, 4], "NORMAL")
        ],
        [
            GameRoom([1, 2, 3], "NORMAL"),
            GameRoom([2, 4], "NORMAL"),
            GameRoom([2, 3, 4], "NORMAL"),
            GameRoom([1, 3, 4], "NORMAL")
        ],
        [
            GameRoom([1, 2, 3], "NORMAL"),
            GameRoom([3, 4], "NORMAL"),
            GameRoom([1], "NORMAL"),
            GameRoom([1], "NORMAL")
        ],
        [
            GameRoom([1], "NORMAL"),
            GameRoom([1, 2], "NORMAL"),
            GameRoom([2, 4], "NORMAL"),
            GameRoom([4], "END")
        ]
    ]

    current_room = maze[int(arguments[0])][int(arguments[1])]

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BASE_PALLETE[current_room.kind]["BACKGROUND"])
        current_room.room_walls().draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
