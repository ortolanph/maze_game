# -*- coding: utf-8 -*-
import argparse
import json
import os

import pygame
from maze_api.maze import Maze

from core.elements.ColorPallete import BASE_PALLETE
from core.elements.HUD import HUD
from core.elements.SkinManager import SkinManager
from core.maze.GameMaze import GameMaze
from core.player.Player import Player

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
    parser.add_argument(
        "--skin",
        help="Selects a Skin",
        type=str,
        default="basic"
    )

    args = parser.parse_args()
    arguments = vars(args)

    print("Verifying arguments")

    my_width = arguments["width"]
    my_height = arguments["height"]
    print_maze = arguments["print_maze"]
    joy_profile = arguments["joy_profile"]
    skin = arguments["skin"]

    if (my_width < 4 or my_width > 999) or (my_height < 4 or my_height > 999):
        print(f"Invalid witdth ({my_width}) or height ({my_height})")
        exit(-1)

    print("Loading skin")
    skin_manager = SkinManager(skin)

    print("Creating Maze")

    generated_maze = Maze(my_width, my_height)
    generated_maze.create_maze()

    if print_maze:
        generated_maze.print_maze()

    print("Converting Maze, creating obstacles")
    maze = GameMaze(skin_manager)
    for y in range(1, my_height + 1):
        for x in range(1, my_width + 1):
            maze.create_room(generated_maze.room_at(x, y))

    print("Initializing game")

    pygame.init()

    print("Loading joystick")
    if joy_profile is not "none":
        for i in range(pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
        for joystick in joysticks:
            joystick.init()

        with open(os.path.join(f"assets/joysticks/{joy_profile}_keys.json"), "r+") as joystick_definition:
            joystick_keys = json.load(joystick_definition)

    # Create an 800x900 sized screen
    print("Openning main window")
    screen = pygame.display.set_mode([800, 900])

    # Set the title of the window
    pygame.display.set_caption('Maze')

    print("Creating HUD")
    hud = HUD()

    print("Creating Player")
    player = Player()
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    print("Creating starting point")
    maze_room = generated_maze.start_room()
    current_room_x = maze_room.x
    current_room_y = maze_room.y
    game_room = maze.room_at(current_room_x, current_room_y)

    clock = pygame.time.Clock()

    print("Ready!")

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

        player.move(game_room)

        if player.rect.x < 0:
            current_room_x -= 1
            player.rect.x = 736

        if player.rect.x > 736:
            current_room_x += 1
            player.rect.x = 0

        if player.rect.y < 0:
            current_room_y -= 1
            player.rect.y = 736

        if player.rect.y > 736:
            current_room_y += 1
            player.rect.y = 0

        screen.blit(skin_manager.get_background(game_room.kind), (0, 0))
        screen.blit(hud, (0, 801))
        hud.update(current_room_x, current_room_y, player.gold)

        movingsprites.draw(screen)

        game_room = maze.room_at(current_room_x, current_room_y)
        game_room.room_walls().draw(screen)

        if len(game_room.items) > 0:
            game_room.items.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
