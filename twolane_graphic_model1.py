import pygame
from time import sleep
import twolane

pygame.init()

traffic_simu=twolane.traffic(n=100,max_v=5,density=0.4,slow_down_random_probability=0.1,generate_car=1)

BLACK = (0,0,0)
WHITE = (255,255,255)

background_colour = (255,255,255)
(width, height) = (1000, 20)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('traffic flow')
screen.fill(background_colour)

pygame.draw.rect(screen, BLACK, [0,0,10,10])
pygame.display.flip()

basicfont = pygame.font.SysFont(None, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    store_string=traffic_simu.iteration().split()
    for j in range(len(store_string)):
        lane=store_string[j]
        for i in range(len(lane)):
            if lane[i]=='~':
                pygame.draw.rect(screen, WHITE, [i*10,10*j,10,10])
            else:
                pygame.draw.rect(screen, (255/5*(5 - int(lane[i])),255/5*(int(lane[i])),0), [i*10,10*j,10,10])



    pygame.display.update()
    pygame.display.flip()
    sleep(1)
