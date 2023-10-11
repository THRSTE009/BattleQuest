import pygame


class Healthbar:
    def __init__(self, screen, x, y, hp, max_hp, red, green):
        self.screen = screen
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

        self.red = red
        self.green = green

    def draw(self, hp):
        self.hp = hp    # Update health as it may have changed since initialization
        width = 150
        height = 20

        # Calculate Green hp bar ratio.
        hp_ratio = self.hp / self.max_hp

        pygame.draw.rect(self.screen, self.red, (self.x, self.y, width, height))
        pygame.draw.rect(self.screen, self.green, (self.x, self.y, width * hp_ratio, height))
