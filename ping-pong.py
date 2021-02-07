import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

pygame.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60

pygame.display.set_caption('Ping Pong')

# assets
img_background = pygame.image.load('assets/background.png').convert()
img_paddle = pygame.image.load('assets/paddle.png').convert()
img_ball = pygame.image.load('assets/ball.png').convert_alpha()

# scale assets to fit screen
img_background = pygame.transform.scale(img_background, (WINDOW_WIDTH, WINDOW_HEIGHT))
img_paddle = pygame.transform.scale(img_paddle, (WINDOW_WIDTH // 50, WINDOW_HEIGHT // 3))
#img_ball = pygame.transform.scale(img_ball, (img_ball.get_width(), img_ball.get_height()))

def main():
    clock = pygame.time.Clock()

    ball_x_pos = WINDOW_WIDTH // 2 - img_ball.get_width() // 2
    ball_y_pos = WINDOW_HEIGHT // 2 - img_ball.get_height() // 2

    player_y_pos = WINDOW_HEIGHT // 2 - img_paddle.get_height() // 2
    computer_y_pos = WINDOW_HEIGHT // 2 - img_paddle.get_height() // 2

    img_ball_rect = img_ball.get_rect(center=(ball_x_pos, ball_y_pos))

    ball_x_velocity = 4
    ball_y_velocity = 4

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        img_ball_rect.centerx += ball_x_velocity
        img_ball_rect.centery += ball_y_velocity
        if img_ball_rect.left <= 0 or img_ball_rect.right >= WINDOW_WIDTH:
            ball_x_velocity *= -1
        if img_ball_rect.top <= 0 or img_ball_rect.bottom >= WINDOW_HEIGHT:
            ball_y_velocity *= -1

        draw(img_ball_rect, player_y_pos, computer_y_pos)

        pygame.display.update()

    pygame.quit()

def draw(ball, player_y_pos, computer_y_pos):
    WIN.blit(img_background, (0, 0))

    WIN.blit(img_paddle, (10, computer_y_pos))
    WIN.blit(img_paddle, (WINDOW_WIDTH - img_paddle.get_width() - 10, player_y_pos))

    WIN.blit(img_ball, ball)

if __name__ == '__main__':
    main()