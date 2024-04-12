import os

import pygame

GAME_NAME = 'Test_task_kodland'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RABBIT_SIZE = (60, 60)
BEE_SIZE = (30, 30)
WORM_SIZE = (80, 60)
FIRE_SIZE = (10, 10)
EGGS_SIZE = (180, 220)

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
RABBIT_LEFT_SIDE = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Rabbit", "rabbit_left_1.png")), RABBIT_SIZE),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Rabbit", "rabbit_left_2.png")), RABBIT_SIZE),
]
RABBIT_RIGHT_SIDE = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Rabbit", "rabbit_right_1.png")), RABBIT_SIZE),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Rabbit", "rabbit_right_2.png")), RABBIT_SIZE),
]
WORM_LEFT_SIDE = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Worm", "worm_1.png")), WORM_SIZE),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Worm", "worm_2.png")), WORM_SIZE)
]
BEE_LEFT_SIDE = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/BEE", "bee_1.png")), BEE_SIZE),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/BEE", "bee_2.png")), BEE_SIZE)
]
FIRE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Fire", "bullet.png")), FIRE_SIZE)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Background.jpg")),
                                    (SCREEN_WIDTH, SCREEN_HEIGHT))
EGGS = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Eggs.png")), EGGS_SIZE)
