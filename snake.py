import pygame


class snake:
    def __init__(self, body_parts: list[tuple], size: tuple, color: tuple):
        self.body = body_parts
        self.size = pygame.Surface(size)
        self.color = color
        self.size.fill(self.color)
        self.direction = None
        self.score = 0

    def change_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[0]

    def grow(self, new_body_part: tuple):
        self.body.append(new_body_part)

    def go_up(self):
        self.body[0] = (self.body[0][0], self.body[0][1] - 10)

    def go_down(self):
        self.body[0] = (self.body[0][0], self.body[0][1] + 10)

    def go_left(self):
        self.body[0] = (self.body[0][0] - 10, self.body[0][1])

    def go_right(self):
        self.body[0] = (self.body[0][0] + 10, self.body[0][1])

    def reposition(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = (self.body[i - 1][0], self.body[i - 1][1])

    def collided(self):
        return self.body[0] in self.body[3:]

    def scored(self):
        self.score += 1


def make_snake(body, size, color):
    return snake(body, size, color)


default_snake = make_snake([(300, 300), (310, 300), (320, 300)], (10, 10), (255, 255, 255))
