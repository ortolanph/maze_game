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
        coin_item = skin["skin"]["items"]["coin"]

        self.images["item"] = dict()
        self.images["item"]["coin"] = pygame.image.load(os.path.join(f"assets/skins/{skin_folder}/images", coin_item))

    def get_item(self, item_name):
        return self.images["item"][item_name]
