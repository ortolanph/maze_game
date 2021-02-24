import json
import os

import pygame


class SkinManager:
    images = dict()

    def __skin_info(self, name, author, mail, description):
        pass

    def __init__(self, skin_name):
        with open(os.path.join(f"assets/skins/{skin_name}.json"), "r+") as skin_definition:
            skin = json.load(skin_definition)

        skin_folder = skin["folder"]
        img_skin_folder = f"assets/skins/{skin_folder}/images"
        fnt_skin_folder = f"assets/skins/{skin_folder}/fonts"

        backgrounds = skin["skin"]["backgrounds"]
        self.images["background"] = dict()
        self.images["background"][1] = pygame.image.load(os.path.join(img_skin_folder, backgrounds["normal"]))
        self.images["background"][2] = pygame.image.load(os.path.join(img_skin_folder, backgrounds["start"]))
        self.images["background"][3] = pygame.image.load(os.path.join(img_skin_folder, backgrounds["end"]))

        coin_item = skin["skin"]["items"]["coin"]
        self.images["item"] = dict()
        self.images["item"]["coin"] = pygame.image.load(os.path.join(img_skin_folder, coin_item))

        hud = skin["skin"]["hud"]
        self.images["hud"] = dict()
        self.images["hud"]["image"] = pygame.image.load(os.path.join(img_skin_folder, hud["image"]))
        self.images["hud"]["font"] = f"{fnt_skin_folder}/{hud['font']}"
        self.images["hud"]["font-size"] = int(hud["font-size"])
        self.images["hud"]["font-color"] = (
            int(hud["font-color"][0]),
            int(hud["font-color"][1]),
            int(hud["font-color"][2])
        )
        self.images["hud"]["background-color"] = (
            int(hud["background-color"][0]),
            int(hud["background-color"][1]),
            int(hud["background-color"][2])
        )

        obstacles = skin["skin"]["obstacles"]
        self.images["obstacles"] = dict()
        self.images["obstacles"]["big-rock"] = pygame.image.load(os.path.join(img_skin_folder, obstacles["big-rock"]))
        self.images["obstacles"]["column"] = pygame.image.load(os.path.join(img_skin_folder, obstacles["column"]))
        self.images["obstacles"]["rock-medium"] = \
            pygame.image.load(os.path.join(img_skin_folder, obstacles["rock-medium"]))
        self.images["obstacles"]["rock-small"] = \
            pygame.image.load(os.path.join(img_skin_folder, obstacles["rock-small"]))

        self.images["obstacles"]["cross-middle"] = \
            pygame.image.load(os.path.join(img_skin_folder, obstacles["column"]))

        cross_arm = pygame.image.load(os.path.join(img_skin_folder, obstacles["cross-arm"]))

        self.images["obstacles"]["cross-arm-north"] = cross_arm
        self.images["obstacles"]["cross-arm-east"] = pygame.transform.rotate(cross_arm, -90)
        self.images["obstacles"]["cross-arm-south"] = pygame.transform.flip(cross_arm, False, True)
        self.images["obstacles"]["cross-arm-west"] = pygame.transform.rotate(cross_arm, 90)

        large_rock = pygame.image.load(os.path.join(img_skin_folder, obstacles["rock-large"]))

        self.images["obstacles"]["rocks-portrait"] = large_rock
        self.images["obstacles"]["rocks-landscape"] = pygame.transform.rotate(large_rock, -90)

    def get_background(self, kind):
        return self.images["background"][kind]

    def get_item(self, item_name):
        return self.images["item"][item_name]

    def get_hud(self):
        return self.images["hud"]

    def get_obstacles(self):
        return self.images["obstacles"]
