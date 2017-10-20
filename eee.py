import pygame
from pygame.constants import QUIT

pygame.init()
screen = pygame.display.set_mode((640, 320))

pygame.display.set_caption("Hello World!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
