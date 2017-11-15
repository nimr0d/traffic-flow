import pygame
from time import sleep
import other

pygame.init()

traffic_simu=other.traffic(n=100,max_v=5,density=0.2,slow_down_random_probability=0.1)

BLACK = (0,0,0)
WHITE = (255,255,255)

background_colour = (255,255,255)
(width, height) = (1000, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('traffic flow')
screen.fill(background_colour)

pygame.draw.rect(screen, BLACK, [0,0,10,10])
pygame.display.flip()

basicfont = pygame.font.SysFont(None, 20)

running = True
store_list_string=[]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    store_string=traffic_simu.iteration()
    store_list_string.append(store_string)
    for j in range(len(store_list_string)):
        store_string=store_list_string[j]
        for i in range(len(store_string)):
            if store_string[i]=='~':
                pygame.draw.rect(screen, WHITE, [i*10,j*10,10,10])
            else:
                pygame.draw.rect(screen, BLACK, [i*10,j*10,10,10])


    if len(store_list_string)>=height/10:
        store_list_string=store_list_string[1:]

    pygame.display.update()
    pygame.display.flip()
    sleep(0.05)
