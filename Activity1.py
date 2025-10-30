import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
Done = False

while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(60,60,250,125),0)
    pygame.draw.circle(screen,(0,10,255),(250,250),30,7)
    pygame.draw.circle(screen,(70,40,180),(400,250),30)


    pygame.display.flip()