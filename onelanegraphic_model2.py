import pygame
import numpy as np
from time import sleep
import onelane

pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)

background_colour = (255,255,255)
(width, height) = (1000, 170)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('traffic flow')
screen.fill(background_colour)

pygame.draw.rect(screen, BLACK, [0,0,10,10])
pygame.display.flip()

basicfont = pygame.font.SysFont(None, 20)

densitys=np.array(range(1,10),dtype=float)/10
traffic_simu=[]
for density in densitys:
    traffic_simu.append(onelane.traffic(n=100,max_v=5,density=density,slow_down_random_probability=0.1))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    store_list_string=[]
    for i in range(9):
        store_list_string.append(traffic_simu[i].iteration())
        store_list_string.append(['~' for j in range(100)])
    for j in range(len(store_list_string)):
        store_string=store_list_string[j]
        for i in range(len(store_string)):
            if store_string[i]=='~':
                pygame.draw.rect(screen, WHITE, [i*10,j*10,10,10])
            else:
                pygame.draw.rect(screen, (255/5*(5 - int(store_string[i])),255/5*(int(store_string[i])),0), [i*10,j*10,10,10])


    pygame.display.update()
    pygame.display.flip()
    sleep(1)
