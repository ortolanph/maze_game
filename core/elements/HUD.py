import pygame


class HUD(pygame.Surface):
    hud_font = None
    hud_skin = dict()

    def __init__(self, hud_skin):
        super().__init__([800, 100])
        self.hud_skin = hud_skin
        self.blit(hud_skin["image"], (0, 0))

        pygame.font.init()
        self.hud_font = pygame.font.Font(hud_skin["font"], hud_skin["font-size"])

    def update(self, x, y, gold):
        my_x = "{:0>3d}".format(x)
        my_y = "{:0>3d}".format(y)
        my_gold = "{:0>8d}".format(gold)

        label_x_coordinate = pygame.font.Font.render(self.hud_font, my_x, True, self.hud_skin["font-color"])
        label_y_coordinate = pygame.font.Font.render(self.hud_font, my_y, True, self.hud_skin["font-color"])
        label_gold_value = pygame.font.Font.render(self.hud_font, my_gold, True, self.hud_skin["font-color"])

        erase_x = pygame.Surface((60, 25))
        erase_x.fill(self.hud_skin["background-color"])
        erase_y = pygame.Surface((60, 25))
        erase_y.fill(self.hud_skin["background-color"])
        erase_gold = pygame.Surface((170, 25))
        erase_gold.fill(self.hud_skin["background-color"])

        self.blit(erase_x, (60, 15))
        self.blit(label_x_coordinate, (60, 15))
        self.blit(erase_y, (60, 55))
        self.blit(label_y_coordinate, (60, 55))
        self.blit(erase_gold, (610, 50))
        self.blit(label_gold_value, (620, 50))
