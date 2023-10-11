import pygame


class Fighter:
    def __init__(self, screen, x, y, name, max_hp, strength, potions):
        self.screen = screen

        self.name = name
        self.max_hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True

        img = pygame.image.load(f"assets/{self.name}/Idle/0.png")
        self.image = pygame.transform.scale(img,
                                            (img.get_width() * 3, img.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
