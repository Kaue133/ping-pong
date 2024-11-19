import pygame
import sys

# Inicialização do Pygame

pygame.init()

# Definição de cores

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

# Configurações da tela

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

FPS = 60

# Configurações dos paddles

PADDLE_WIDTH = 10

PADDLE_HEIGHT = 100

PADDLE_SPEED = 5

# Inicialização da tela

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pong')

# Definição dos objetos do jogo

player1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                      PADDLE_HEIGHT)

ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)

ball_speed_x = 7

ball_speed_y = 7

# Loop principal do jogo

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

    # Movimentação dos paddles

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED

    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += PADDLE_SPEED

    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED

    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += PADDLE_SPEED

    # Movimentação da bola

    ball.x += ball_speed_x

    ball.y += ball_speed_y

    # Colisões com as paredes

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x

    # Colisões com os paddles

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x

    # Limpeza da tela

    screen.fill(BLACK)

    # Desenho dos objetos do jogo

    pygame.draw.rect(screen, WHITE, player1)

    pygame.draw.rect(screen, WHITE, player2)

    pygame.draw.ellipse(screen, WHITE, ball)

    # Atualização da tela

    pygame.display.flip()

    # Controle de FPS

    pygame.time.Clock().tick(FPS)