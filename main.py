import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

#Game window creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and food creation
snake = [(100, 100)]
direction = (BLOCK_SIZE, 0)
food = (random.randint(0, WIDTH//BLOCK_SIZE-1) * BLOCK_SIZE, random.randint(0, HEIGHT//BLOCK_SIZE-1) * BLOCK_SIZE)
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)

    # Snake movement
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head in snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        running = False  # Game over condition
    else:
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, WIDTH//BLOCK_SIZE-1) * BLOCK_SIZE, random.randint(0, HEIGHT//BLOCK_SIZE-1) * BLOCK_SIZE)
        else:
            snake.pop()

    # Illustration of snake and food
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
