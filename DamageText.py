import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour, font):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        # Float text upwards
        self.rect.y -= 1
        # Delete text after a few seconds.
        self.counter += 1
        if self.counter > 30:
            self.kill()
