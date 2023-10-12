import pygame
import random
from DamageText import DamageText


class Fighter:
    def __init__(self, screen, x, y, name, max_hp, strength, potions, red, font, damage_text_group):
        self.screen = screen

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True

        self.animation_list = []    # Master list for all animations.
        self.frame_index = 0
        self.action = 0     # 0 = idle, 1 = attack, 2 = hurt, 3 = death.
        self.update_time = pygame.time.get_ticks()

        self.red = red
        self.font = font
        self.damage_text_group = damage_text_group

        self.load_animations("Idle", 8)  # Load idle images
        self.load_animations("Attack", 8)  # Load Attack images
        self.load_animations("Hurt", 3)   # Load Hurt images
        self.load_animations("Death", 10)   # Load Death images

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Load idle images
    def load_animations(self, action, number_of_images):
        temp_list = []
        for i in range(number_of_images):
            loaded_img = pygame.image.load(f"assets/{self.name}/{action}/{i}.png")
            scaled_img = pygame.transform.scale(loaded_img,
                                                (loaded_img.get_width() * 3, loaded_img.get_height() * 3))
            temp_list.append(scaled_img)

        self.animation_list.append(temp_list)

    def update(self):
        animation_cooldown = 100
        # Handle animation
        # Update image
        self.image = self.animation_list[self.action][self.frame_index]  # Get the latest image.
        current_time = pygame.time.get_ticks()

        if current_time - self.update_time > animation_cooldown:
            self.update_time = current_time
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        # set  variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        # Deal damage to an enemy.
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        target.hurt()

        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), self.red, self.font)
        self.damage_text_group.add(damage_text)

        # Check if target died.
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()

        # set  variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        # set  variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # set  variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_potions
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        self.screen.blit(self.image, self.rect)

