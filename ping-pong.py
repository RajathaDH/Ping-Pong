import random
import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

pygame.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60

BALL_SPEED = 8
PLAYER_SPEED = 8

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

    player_y_pos = WINDOW_HEIGHT // 2
    computer_y_pos = WINDOW_HEIGHT // 2

    ball_container = img_ball.get_rect(center=(ball_x_pos, ball_y_pos))
    player_container = img_paddle.get_rect(center=(WINDOW_WIDTH - img_paddle.get_width() // 2 - 10, player_y_pos))
    computer_container = img_paddle.get_rect(center=(img_paddle.get_width() // 2 + 10, computer_y_pos))

    ball_x_velocity = BALL_SPEED * random.choice((1, -1))
    ball_y_velocity = BALL_SPEED * random.choice((1, -1))
    player_velocity = 0

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_velocity -= PLAYER_SPEED
                if event.key == pygame.K_DOWN:
                    player_velocity += PLAYER_SPEED
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_velocity = 0
                if event.key == pygame.K_DOWN:
                    player_velocity = 0

        player_container.centery += player_velocity

        ball_container.centerx += ball_x_velocity
        ball_container.centery += ball_y_velocity

        # check collision with side walls and reset game
        if ball_container.left <= 0 or ball_container.right >= WINDOW_WIDTH:
            ball_container.center = (ball_x_pos, ball_y_pos)
            ball_x_velocity = BALL_SPEED * random.choice((1, -1))
            ball_y_velocity = BALL_SPEED * random.choice((1, -1))
        
        # check collision with top and bottom
        if ball_container.top <= 0 or ball_container.bottom >= WINDOW_HEIGHT:
            ball_y_velocity *= -1
        
        # check collision with paddle
        if ball_container.colliderect(player_container) or ball_container.colliderect(computer_container):
            ball_x_velocity *= -1

        draw(ball_container, player_container, computer_container)

        pygame.display.update()

    pygame.quit()

def draw(ball, player_container, computer_container):
    WIN.blit(img_background, (0, 0))

    WIN.blit(img_paddle, player_container)
    WIN.blit(img_paddle, computer_container)

    WIN.blit(img_ball, ball)

if __name__ == '__main__':
    main()