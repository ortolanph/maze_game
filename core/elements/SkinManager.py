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

        backgrounds = skin["skin"]["backgrounds"]
        self.images["background"] = dict()
        self.images["background"][1] = pygame.image.load(os.path.join(img_skin_folder, backgrounds["normal"]))
        self.images["background"][2] = pygame.image.load(os.path.join(img_skin_folder, backgrounds["start"]))
        self.images["background"][3] = pygame.image.load(os.path.join(img_skin_folder, backgrounds["end"]))

        coin_item = skin["skin"]["items"]["coin"]
        self.images["item"] = dict()
        self.images["item"]["coin"] = pygame.image.load(os.path.join(img_skin_folder, coin_item))

    def get_background(self, kind):
        return self.images["background"][kind]

    def get_item(self, item_name):
        return self.images["item"][item_name]
