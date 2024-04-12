from variables import FIRE, SCREEN, SCREEN_WIDTH


class Bullet:
    def __init__(self, x, y, direction):
        if direction == -1:
            self.x = x
            self.y = y + 35
        if direction == 1:
            self.x = x + 40
            self.y = y + 35
        self.direction = direction

    def draw_bullet(self):
        SCREEN.blit(FIRE, (self.x, self.y))

    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not (0 <= self.x <= SCREEN_WIDTH)
