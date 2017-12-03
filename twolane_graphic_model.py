import pygame
from time import sleep
import twolane

pygame.init()

traffic_simu=twolane.traffic(n=100,max_v=5,density=0.4,slow_down_random_probability=0.1)

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
count=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    store_string=traffic_simu.iteration().split()
    lane0=store_string[0]
    lane1=store_string[1]
    for i in range(len(lane0)):
        if lane0[i]=='~':
            pygame.draw.rect(screen, WHITE, [i*10,0,10,10])
        else:
            pygame.draw.rect(screen, (255/5*(5 - int(lane0[i])),255/5*(int(lane0[i])),0), [i*10,0,10,10])

    for i in range(len(lane1)):
        if lane1[i]=='~':
            pygame.draw.rect(screen, WHITE, [i*10,10,10,10])
        else:
            pygame.draw.rect(screen, (255/5*(5 - int(lane1[i])),255/5*(int(lane1[i])),0), [i*10,10,10,10])


    pygame.display.update()
    pygame.display.flip()
    sleep(1)
