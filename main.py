import snake
import apple

import pygame
from pygame.locals import *


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def ate(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def check_edges(a_snake):
    head = a_snake.head()
    return head[0] >= 600 or head[1] >= 600 or head[0] <= 0 or head[1] <= 0

def main():
    game_snake = snake.default_snake
    game_clock = pygame.time.Clock()
    game_apple = apple.default_apple
    run(game_snake, game_apple, game_clock)

def run(a_snake: snake.snake, a_apple: apple.apple, clock):
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    if a_snake.direction != DOWN:
                        a_snake.change_direction(UP)
                elif event.key == K_DOWN or event.key == K_s:
                    if a_snake.direction != UP:
                        a_snake.change_direction(DOWN)
                elif event.key == K_LEFT or event.key == K_a:
                    if a_snake.direction != RIGHT:
                        a_snake.change_direction(LEFT)
                elif event.key == K_RIGHT or event.key == K_d:
                    if a_snake.direction != LEFT:
                        a_snake.change_direction(RIGHT)

        if ate(a_snake.head(), a_apple.position):
            a_apple.change_position()
            a_snake.grow((0, 0))
            a_snake.scored()

        if check_edges(a_snake):
            pygame.quit()

        if a_snake.direction == UP:
            a_snake.go_up()
        if a_snake.direction == DOWN:
            a_snake.go_down()
        if a_snake.direction == LEFT:
            a_snake.go_left()
        if a_snake.direction == RIGHT:
            a_snake.go_right()

        if a_snake.collided():
            pygame.quit()

        a_snake.reposition()

        black_color = (0, 0, 0)
        screen.fill(black_color)
        screen.blit(a_apple.size, a_apple.position)

        for position in a_snake.body:
            screen.blit(a_snake.size, position)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake Game")
    main()
