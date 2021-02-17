# -*- coding: utf-8 -*-
import argparse
import sys
import os
import json

import pygame
from maze_api.maze import Maze

from core.ColorPallete import BASE_PALLETE
from core.GameRoom import GameRoom
from core.Player import Player

arguments = sys.argv[1:]
PLAYER_STEP = 10
joysticks = []


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    parser = argparse.ArgumentParser(
        prog="mazegame",
        description="Creates a Maze Game session",
        epilog="Be challenged!"
    )
    parser.add_argument(
        "--width",
        help="Width of the maze (min = 4 and max = 999)",
        type=int,
        default=5
    )
    parser.add_argument(
        "--height",
        help="Height of the maze (min = 4 and max = 999)",
        type=int,
        default=5
    )
    parser.add_argument(
        "--joy-profile",
        help="Loads a Joystick Profile (ps4, xbox, airflo)",
        type=str,
        default="none",
        choices=["none", "ps4", "xbox", "airflo"]
    )
    parser.add_argument(
        "--print-maze",
        help="Prints the Maze",
        type=bool,
        default=False
    )
    args = parser.parse_args()
    arguments = vars(args)

    my_width = arguments["width"]
    my_height = arguments["height"]
    print_maze = arguments["print_maze"]
    joy_profile = arguments['joy_profile']

    if (my_width < 4 or my_width > 999) or (my_height < 4 or my_height > 999):
        print(f"Invalid witdth ({my_width}) or height ({my_height})")
        exit(-1)

    pygame.init()

    if joy_profile is not "none":
        for i in range(pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
        for joystick in joysticks:
            joystick.init()

        with open(os.path.join(f"assets/joysticks/{joy_profile}_keys.json"), "r+") as joystick_definition:
            joystick_keys = json.load(joystick_definition)

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 800])

    # Set the title of the window
    pygame.display.set_caption('Maze')

    maze = Maze(my_width, my_height)
    maze.create_maze()

    if print_maze:
        maze.print_maze()

    player = Player()
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    maze_room = maze.start_room()
    current_room_x = maze_room.x
    current_room_y = maze_room.y
    game_room = GameRoom(maze_room.exits, maze_room.kind)

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.JOYHATMOTION:
                if event.value == (-1, 0):
                    player.changespeed(-PLAYER_STEP, 0)
                if event.value == (1, 0):
                    player.changespeed(PLAYER_STEP, 0)
                if event.value == (0, 1):
                    player.changespeed(0, -PLAYER_STEP)
                if event.value == (0, -1):
                    player.changespeed(0, PLAYER_STEP)
                if event.value == (0, 0):
                    player.stop()

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

        player.move(game_room.room_walls())

        if player.rect.x < -64:
            current_room_x -= 1
            player.rect.x = 790
            maze_room = maze.room_at(current_room_x, current_room_y)

        if player.rect.x > 801:
            current_room_x += 1
            player.rect.x = 0
            maze_room = maze.room_at(current_room_x, current_room_y)

        if player.rect.y < -64:
            current_room_y -= 1
            player.rect.y = 790
            maze_room = maze.room_at(current_room_x, current_room_y)

        if player.rect.y > 801:
            current_room_y += 1
            player.rect.y = 0
            maze_room = maze.room_at(current_room_x, current_room_y)

        screen.fill(BASE_PALLETE[game_room.kind]["BACKGROUND"])

        movingsprites.draw(screen)
        game_room = GameRoom(maze_room.exits, maze_room.kind)
        game_room.room_walls().draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
