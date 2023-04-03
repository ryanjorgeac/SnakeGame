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
    pygame.init()
    game_screen = pygame.display.set_mode((600, 600))
    game_screen.fill((0, 0, 0))
    pygame.display.set_caption("Snake Game")
    game_snake = snake.default_snake
    game_clock = pygame.time.Clock()
    game_apple = apple.default_apple
    start_menu(game_screen)
    run(game_screen, game_snake, game_apple, game_clock)


def start_menu(a_screen):
    a_screen.fill((0, 0, 0))
    screen_width = a_screen.get_width()
    screen_height = a_screen.get_height()
    title_font = pygame.font.Font('./Fonts/Cocogoose Pro Light-trial.ttf', 50)
    title = title_font.render('>> Snake Game <<', True, (255, 255, 255))
    start_font = pygame.font.Font('./Fonts/Cocogoose Pro Light-trial.ttf', 30)
    start_button = start_font.render('(Press Space to start)', True, (255, 255, 255))

    to_game = False
    while not to_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                to_game = True
                break

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    to_game = True
                    break

        a_screen.blit(title, (screen_width / 2 - title.get_width() / 2, screen_height / 2 - title.get_height()))
        a_screen.blit(start_button, (screen_width / 2 - start_button.get_width() / 2, screen_height / 2 + start_button.get_height() / 4))
        pygame.display.update()


def run(a_screen, a_snake: snake.snake, a_apple: apple.apple, clock):
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    if a_snake.direction != DOWN:
                        a_snake.change_direction(UP)
                if event.key == K_DOWN or event.key == K_s:
                    if a_snake.direction != UP:
                        a_snake.change_direction(DOWN)
                if event.key == K_LEFT or event.key == K_a:
                    if a_snake.direction != RIGHT:
                        a_snake.change_direction(LEFT)
                if event.key == K_RIGHT or event.key == K_d:
                    if a_snake.direction != LEFT:
                        a_snake.change_direction(RIGHT)
                if event.key == K_ESCAPE:
                    pass
                    # pause_screen()

        if ate(a_snake.head(), a_apple.position):
            a_apple.change_position()
            a_snake.grow((0, 0))
            a_snake.scored()

        if check_edges(a_snake) or a_snake.collided():
            break

        if a_snake.direction == UP:
            a_snake.go_up()
        if a_snake.direction == DOWN:
            a_snake.go_down()
        if a_snake.direction == LEFT:
            a_snake.go_left()
        if a_snake.direction == RIGHT:
            a_snake.go_right()

        a_snake.reposition()

        black_color = (0, 0, 0)
        a_screen.fill(black_color)
        a_screen.blit(a_apple.size, a_apple.position)

        score_render(a_screen, a_snake.score)

        for position in a_snake.body:
            a_screen.blit(a_snake.size, position)

        pygame.display.update()

    if game_over_screen(a_screen):
        main()


def game_over_screen(a_screen):
    a_screen.fill((0, 0, 0))
    font = pygame.font.Font('./Fonts/Cocogoose Pro Light-trial.ttf', 70)
    title = font.render('Game Over', True, (255, 255, 255))
    r_and_q_font = pygame.font.Font('./Fonts/Cocogoose Pro Light-trial.ttf', 30)
    restart_button = r_and_q_font.render('Space - Restart', True, (255, 255, 255))
    quit_button = r_and_q_font.render('Q - Quit', True, (255, 255, 255))
    screen_width = a_screen.get_width()
    screen_height = a_screen.get_height()
    a_screen.blit(title, (screen_width / 2 - title.get_width() / 2, screen_height / 2 - title.get_height()))
    a_screen.blit(restart_button, (screen_width / 2 - restart_button.get_width() / 2, screen_height / 1.8 - restart_button.get_height()))
    a_screen.blit(quit_button, (screen_width / 2 - quit_button.get_width() / 2, screen_height / 1.9 + quit_button.get_height() / 2))
    pygame.display.update()
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                elif event.key == K_SPACE:
                    over = False
                    break

    return True

def score_render(screen, score: int):
    score_font = pygame.font.SysFont('arial', 18)
    score_rendered = score_font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_rendered.get_rect()
    score_rect.center = (600 / 2, 20)
    screen.blit(score_rendered, score_rect)


if __name__ == "__main__":
    main()
