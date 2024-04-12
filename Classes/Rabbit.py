import pygame

from Classes.Bullet import Bullet
from variables import RABBIT_LEFT_SIDE, RABBIT_RIGHT_SIDE, SCREEN_WIDTH


class Rabbit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 10
        self.velocity_y = 6
        self.face_right = True
        self.face_left = False
        self.step = 0

        self.jump = False

        self.bullets = []
        self.cool_down_count = 0

        self.life_counter = (self.x, self.y, 64, 64)
        self.health = 30
        self.lives = 1
        self.alive = True

    def move_hero(self, buttons):
        if buttons[pygame.K_RIGHT] and self.x <= SCREEN_WIDTH - 62:
            self.x += self.velocity_x
            self.face_right = True
            self.face_left = False
        elif buttons[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velocity_x
            self.face_right = False
            self.face_left = True
        else:
            self.step = 0

    def draw(self, screen):
        self.life_counter = (self.x + 15, self.y + 15, 30, 40)
        pygame.draw.rect(screen, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.health >= 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        if self.step >= 2:
            self.step = 0
        if self.face_left:
            screen.blit(RABBIT_LEFT_SIDE[self.step], (self.x, self.y))
            self.step += 1
        if self.face_right:
            screen.blit(RABBIT_RIGHT_SIDE[self.step], (self.x, self.y))
            self.step += 1

    def jump_motion(self, buttons):
        if buttons[pygame.K_SPACE] or buttons[pygame.K_UP] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.velocity_y * 4
            self.velocity_y -= 1
        if self.velocity_y < -6:
            self.jump = False
            self.velocity_y = 6

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self, buttons, enemies, rabbit, FIRE_SOUND):
        for enemy in enemies:
            for bullet in self.bullets:
                if enemy.life_counter[0] < bullet.x < enemy.life_counter[0] + enemy.life_counter[2] and \
                        enemy.life_counter[1] < bullet.y < \
                        enemy.life_counter[1] + enemy.life_counter[3]:
                    enemy.health -= 5
                    rabbit.bullets.remove(bullet)

        self.cooldown()
        if buttons[pygame.K_f] and self.cool_down_count == 0:
            FIRE_SOUND.play()
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

