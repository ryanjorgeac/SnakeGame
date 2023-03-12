import pygame
import random


class apple:
    def __init__(self, size: tuple[int, int], color: tuple[int, int, int]):
        self.size = pygame.Surface(size)
        self.size.fill(color)
        self.position = self.new_position()

    def new_position(self):
        x = random.randint(0, 590)
        y = random.randint(0, 590)
        return x // 10 * 10, y // 10 * 10

    def change_position(self):
        self.position = self.new_position()


def make_apple(a_size, a_color):
    return apple(a_size, a_color)


apple_size = (10, 10)
apple_color = (255, 0, 0)
default_apple = make_apple(apple_size, apple_color)
