import sys
import pygame
from pygame.locals import *
from constants import *

pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1600, 1000))
pygame.display.set_caption("PyGame")
clock = pygame.time.Clock()

class Pr(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("srprs.png")
        self.rect = self.image.get_rect()
        self.rect.center = (775, 1250)

    def move(self, keys):
        dx = 0
        dy = 0
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        if keys[pygame.K_UP]:
            dy = -5
        if keys[pygame.K_DOWN]:
            dy = 5
        self.rect.move_ip(dx, dy)

pr = Pr()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    pr.move(keys)

    win.fill((255, 255, 255))
    win.blit(pygame.image.load("jngl.png"), (0, 0))
    win.blit(pr.image, pr.rect)

    pygame.display.update()
    clock.tick(60)
