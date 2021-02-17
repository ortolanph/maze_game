# -*- coding: utf-8 -*-
import sys

import pygame

from ColorPallete import BASE_PALLETE
from GameRoom import GameRoom
from Player import Player

arguments = sys.argv[1:]
PLAYER_STEP = 10


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

    player = Player()
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    current_room_x = 1
    current_room_y = 0
    current_room = maze[int(current_room_y)][int(current_room_x)]

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-PLAYER_STEP, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(PLAYER_STEP, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -PLAYER_STEP)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, PLAYER_STEP)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(PLAYER_STEP, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-PLAYER_STEP, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, PLAYER_STEP)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -PLAYER_STEP)

        player.move(current_room.room_walls())

        if player.rect.x < -64:
            current_room_x -= 1
            player.rect.x = 790

        if player.rect.x > 801:
            current_room_x += 1
            player.rect.x = 0

        if player.rect.y < -64:
            current_room_y -= 1
            player.rect.y = 790

        if player.rect.y > 801:
            current_room_y += 1
            player.rect.y = 0

        current_room = maze[int(current_room_y)][int(current_room_x)]
        screen.fill(BASE_PALLETE[current_room.kind]["BACKGROUND"])

        movingsprites.draw(screen)
        current_room.room_walls().draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
