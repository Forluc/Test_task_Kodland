import os
import random
import sys

import pygame
from environs import Env

from Classes.Enemy import Enemy
from Classes.Rabbit import Rabbit
from variables import (BACKGROUND, BEE_LEFT_SIDE, BLACK, EGGS, GAME_NAME,
                       SCREEN, WHITE, WORM_LEFT_SIDE)


def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play(-1)


def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, True, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)


def start_game(FIRE_SOUND, tower_health, enemies_speed):
    rabbit = Rabbit(250, 290)

    enemies = []
    kill_counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        buttons = pygame.key.get_pressed()

        rabbit.shoot(buttons, enemies, rabbit, FIRE_SOUND)
        rabbit.move_hero(buttons)
        rabbit.jump_motion(buttons)

        if tower_health == 0:
            rabbit.alive = False

        if len(enemies) == 0:
            enemies.append(Enemy(750, 280, enemies_speed, WORM_LEFT_SIDE))
            enemies.append(Enemy(750, random.randint(200, 250), enemies_speed, BEE_LEFT_SIDE))
            if enemies_speed <= 10:
                enemies_speed += 0.25
        for enemy in enemies:
            enemy.move(rabbit, enemy)
            if enemy.off_screen() or enemy.health == 0:
                enemies.remove(enemy)
            if enemy.x < 50:
                enemies.remove(enemy)
                tower_health -= 1
            if enemy.health == 0:
                kill_counter += 1

        # DRAW
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(EGGS, (-100, 170))

        for bullet in rabbit.bullets:
            bullet.draw_bullet()

        for enemy in enemies:
            enemy.draw(SCREEN)

        rabbit.draw(SCREEN)
        if not rabbit.alive:
            SCREEN.fill(BLACK)
            font = pygame.font.Font(None, 48)
            text = font.render('Ты проиграл, нажми M или закрой', True, WHITE)
            SCREEN.blit(text, (120, 50))
            if buttons[pygame.K_m]:
                return

        font = pygame.font.Font(None, 48)
        text = font.render(
            f'Жизнь: {str(rabbit.lives)} | Осталось яиц: {str(tower_health)} | Убито: {str(kill_counter)}',
            True, BLACK)
        SCREEN.blit(text, (100, 20))

        pygame.time.delay(30)
        pygame.display.update()


def main():
    env = Env()
    env.read_env()
    enemies_speed = env.int('ENEMIES_SPEED', 2)
    eggs_health = env.int('EGGS_HEALTH', 2)

    pygame.init()
    pygame.display.set_caption(GAME_NAME)

    FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'fire_sound.mp3'))
    pygame.mixer.music.load(os.path.join('Assets', 'Audio', 'background_sound.mp3'))
    pygame.mixer.music.play(-1)

    running = True
    while running:
        SCREEN.blit(BACKGROUND, (0, 0))

        font = pygame.font.Font(None, 36)
        draw_text('Start Game', font, BLACK, SCREEN, 300, 100)
        draw_text('Music ON/OFF', font, BLACK, SCREEN, 300, 200)
        draw_text('Quit', font, BLACK, SCREEN, 300, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if 300 <= mx <= 470 and 100 <= my <= 150:
                        start_game(FIRE_SOUND, eggs_health, enemies_speed)
                    elif 300 <= mx <= 470 and 200 <= my <= 250:
                        toggle_music()
                    elif 300 <= mx <= 350 and 300 <= my <= 350:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
