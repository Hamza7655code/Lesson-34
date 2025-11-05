import pygame

pygame.init()

screen = pygame.display.set_mode((540, 480))
pygame.display.set_caption("Shapes Example")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 50)
text = font.render("Hello world!", True, WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    screen.blit(text, (330, 220))

    pygame.draw.rect(screen, GREEN, (50, 50, 100, 100))
    pygame.draw.circle(screen, RED, (450, 100), 50)
    pygame.draw.circle(screen, YELLOW, (100, 380), 50, 5)
    pygame.draw.rect(screen, BLUE, (420, 360, 40, 40))

    pygame.display.flip()

pygame.quit()