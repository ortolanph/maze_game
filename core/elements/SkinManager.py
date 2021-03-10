import json
import os

import pygame


class SkinManager:
    __images = dict()
    __img_skin_folder = ""
    __fnt_skin_folder = ""

    def __skin_info(self, name, author, mail, description):
        skin_info = f"""
Skin {name}
Author.......: {author}
e-Mail.......: {mail}
Description..: {description}
"""
        print(skin_info)

    def __init__(self, skin_name):
        with open(os.path.join(f"assets/skins/{skin_name}.json"), "r+") as skin_definition:
            skin = json.load(skin_definition)

        self.__skin_info(skin["name"], skin["author"], skin["mail"], skin["description"])

        skin_folder = skin["folder"]
        self.__img_skin_folder = f"assets/skins/{skin_folder}/images"
        self.__fnt_skin_folder = f"assets/skins/{skin_folder}/fonts"

        backgrounds = skin["skin"]["backgrounds"]
        self.__load_backgrounds(backgrounds)

        items = skin["skin"]["items"]
        self.__load_items(items)

        hud = skin["skin"]["hud"]
        self.__load_hud(hud)

        obstacles = skin["skin"]["obstacles"]
        self.__load_obstacles(obstacles)

        walls = skin["skin"]["walls"]
        self.__load_walls(walls)

    def __load_backgrounds(self, backgrounds):
        self.__images["background"] = dict()
        self.__images["background"][1] = pygame.image.load(os.path.join(self.__img_skin_folder, backgrounds["normal"]))
        self.__images["background"][2] = pygame.image.load(os.path.join(self.__img_skin_folder, backgrounds["start"]))
        self.__images["background"][3] = pygame.image.load(os.path.join(self.__img_skin_folder, backgrounds["end"]))

    def get_background(self, kind):
        return self.__images["background"][kind]

    def __load_items(self, items):
        self.__images["item"] = dict()
        self.__images["item"]["coin"] = pygame.image.load(os.path.join(self.__img_skin_folder, items["coin"]))

    def get_item(self, item_name):
        return self.__images["item"][item_name]

    def __load_hud(self, hud):
        self.__images["hud"] = dict()
        self.__images["hud"]["image"] = pygame.image.load(os.path.join(self.__img_skin_folder, hud["image"]))
        self.__images["hud"]["font"] = f"{self.__fnt_skin_folder}/{hud['font']}"
        self.__images["hud"]["font-size"] = int(hud["font-size"])
        self.__images["hud"]["font-color"] = (
            int(hud["font-color"][0]),
            int(hud["font-color"][1]),
            int(hud["font-color"][2])
        )
        self.__images["hud"]["background-color"] = (
            int(hud["background-color"][0]),
            int(hud["background-color"][1]),
            int(hud["background-color"][2])
        )

    def get_hud(self):
        return self.__images["hud"]

    def __load_obstacles(self, obstacles):
        self.__images["obstacles"] = dict()
        self.__images["obstacles"]["big-rock"] = \
            pygame.image.load(os.path.join(self.__img_skin_folder, obstacles["big-rock"]))
        self.__images["obstacles"]["column"] = \
            pygame.image.load(os.path.join(self.__img_skin_folder, obstacles["column"]))
        self.__images["obstacles"]["rock-medium"] = \
            pygame.image.load(os.path.join(self.__img_skin_folder, obstacles["rock-medium"]))
        self.__images["obstacles"]["rock-small"] = \
            pygame.image.load(os.path.join(self.__img_skin_folder, obstacles["rock-small"]))

        self.__images["obstacles"]["cross-middle"] = \
            pygame.image.load(os.path.join(self.__img_skin_folder, obstacles["column"]))

        cross_arm = pygame.image.load(
            os.path.join(self.__img_skin_folder, obstacles["cross-arm"]))

        self.__images["obstacles"]["cross-middle"] = pygame.image.load(
            os.path.join(self.__img_skin_folder, obstacles["cross-middle"]))
        self.__images["obstacles"]["cross-arm-north"] = cross_arm
        self.__images["obstacles"]["cross-arm-east"] = pygame.transform.rotate(cross_arm, -90)
        self.__images["obstacles"]["cross-arm-south"] = pygame.transform.flip(cross_arm, False, True)
        self.__images["obstacles"]["cross-arm-west"] = pygame.transform.rotate(cross_arm, 90)

        large_rock = pygame.image.load(os.path.join(self.__img_skin_folder, obstacles["rock-large"]))

        self.__images["obstacles"]["rocks-portrait"] = large_rock
        self.__images["obstacles"]["rocks-landscape"] = pygame.transform.rotate(large_rock, -90)

    def get_obstacles(self):
        return self.__images["obstacles"]

    def __load_walls(self, walls):
        self.__images["walls"] = dict()

        corner = pygame.image.load(os.path.join(self.__img_skin_folder, walls["corner"]))
        wall = pygame.image.load(os.path.join(self.__img_skin_folder, walls["wall"]))
        exit_wall = pygame.image.load(os.path.join(self.__img_skin_folder, walls["exit-wall"]))
        exit_step = pygame.image.load(os.path.join(self.__img_skin_folder, walls["exit-step"]))

        self.__images["walls"]["corners"] = [
            corner,
            pygame.transform.flip(corner, True, False),
            pygame.transform.flip(corner, True, True),
            pygame.transform.flip(corner, False, True),
        ]

        self.__images["walls"]["exits"] = {
            1: [
                exit_wall,
                pygame.transform.flip(exit_wall, True, False)
            ],
            2: [
                pygame.transform.rotate(exit_wall, -90),
                pygame.transform.flip(pygame.transform.rotate(exit_wall, -90), False, True)
            ],
            3: [
                pygame.transform.flip(exit_wall, False, True),
                pygame.transform.rotate(exit_wall, 180)
            ],
            4: [
                pygame.transform.flip(pygame.transform.rotate(exit_wall, 90), False, True),
                pygame.transform.flip(pygame.transform.rotate(exit_wall, 270), True, True)
            ]
        }

        self.__images["walls"]["hard-walls"] = {
            1: wall,
            2: pygame.transform.rotate(wall, -90),
            3: pygame.transform.flip(wall, True, True),
            4: pygame.transform.rotate(wall, 90)
        }

        self.__images["walls"]["exit-steps"] = {
            1: exit_step,
            2: pygame.transform.rotate(exit_step, -90),
            3: pygame.transform.flip(exit_step, True, True),
            4: pygame.transform.rotate(exit_step, 90)
        }

    def get_walls(self):
        return  self.__images["walls"]
