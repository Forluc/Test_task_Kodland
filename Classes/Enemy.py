import pygame

from variables import SCREEN_WIDTH


class Enemy:
    def __init__(self, x, y, speed, enemy):
        self.x = x
        self.y = y
        self.speed = speed
        self.step = 0

        self.life_counter = (self.x, self.y, 64, 64)
        self.health = 30
        self.enemy = enemy

    def draw(self, screen):
        self.life_counter = (self.x + 20, self.y + 10, 30, 45)
        pygame.draw.rect(screen, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.health >= 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        if self.step >= 2:
            self.step = 0
        screen.blit(self.enemy[self.step], (self.x, self.y))
        self.step += 1

    def move(self, rabbit, enemy):
        if rabbit.life_counter[0] < enemy.x + 32 < rabbit.life_counter[0] + rabbit.life_counter[2] and rabbit.life_counter[1] < enemy.y + 32 < \
                rabbit.life_counter[1] + rabbit.life_counter[3]:
            if rabbit.health > 0:
                rabbit.health -= 1
                if rabbit.health == 0 and rabbit.lives > 0:
                    rabbit.lives -= 1
                    rabbit.health = 30
                elif rabbit.health == 0 and rabbit.lives == 0:
                    rabbit.alive = False

        self.x -= self.speed

    def off_screen(self):
        return not (0 <= self.x <= SCREEN_WIDTH)
