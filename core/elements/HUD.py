import pygame
from core.elements.ColorPallete import BASE_PALLETE


class HUD(pygame.Surface):

    hud_font = None

    def __init__(self):
        super().__init__([800, 100])
        self.fill(BASE_PALLETE["HUD"]["BACKGROUND"])

        pygame.font.init()
        self.hud_font = pygame.font.Font("assets/fonts/ka1.ttf", 20)

        label_x = pygame.font.Font.render(self.hud_font, "X", True, BASE_PALLETE["HUD"]["FONT_COLOR"])
        label_y = pygame.font.Font.render(self.hud_font, "Y", True, BASE_PALLETE["HUD"]["FONT_COLOR"])
        label_gold = pygame.font.Font.render(self.hud_font, "GOLD", True, BASE_PALLETE["HUD"]["FONT_COLOR"])

        self.blit(label_x, (25, 15))
        self.blit(label_y, (25, 55))
        self.blit(label_gold, (650, 15))

    def update(self, x, y, gold):
        my_x = "{:0>3d}".format(x)
        my_y = "{:0>3d}".format(y)
        my_gold = "{:0>8d}".format(gold)

        label_x_coordinate = pygame.font.Font.render(self.hud_font, my_x, True, BASE_PALLETE["HUD"]["FONT_COLOR"])
        label_y_coordinate = pygame.font.Font.render(self.hud_font, my_y, True, BASE_PALLETE["HUD"]["FONT_COLOR"])
        label_gold_value = pygame.font.Font.render(self.hud_font, my_gold, True, BASE_PALLETE["HUD"]["FONT_COLOR"])

        erase_x = pygame.Surface((100, 25))
        erase_x.fill(BASE_PALLETE["HUD"]["BACKGROUND"])
        erase_y = pygame.Surface((100, 25))
        erase_y.fill(BASE_PALLETE["HUD"]["BACKGROUND"])
        erase_gold = pygame.Surface((180, 25))
        erase_gold.fill(BASE_PALLETE["HUD"]["BACKGROUND"])

        self.blit(erase_x, (60, 15))
        self.blit(label_x_coordinate, (60, 15))
        self.blit(erase_y, (60, 55))
        self.blit(label_y_coordinate, (60, 55))
        self.blit(erase_gold, (610, 50))
        self.blit(label_gold_value, (620, 50))
