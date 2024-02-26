import pygame
import random

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 2
        self.image = pygame.transform.scale(pygame.image.load('julmust.jpg'), (60, 350))
        self.imageTop = pygame.transform.scale(pygame.image.load('julmust.jpg'), (60, 350))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.rectTop = self.imageTop.get_rect()
        self.rectTop.center = (self.x, self.y)

    def update(self):
        self.x -= self.velocity
        self.rect.center = (self.x, self.y)
        self.rectTop.center = (self.x, self.y)
        self.rectTop.bottom = self.rect.top - 210

        if self.x < 0:
            self.x = 350
            self.changeSize()

    def changeSize(self):
        # Adjust the y-coordinate randomly within a certain range
        if(self.y == 440):
            self.y = 600 + random.randrange(-50,50)
        else:
            self.y = 440

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.imageTop, self.rectTop)
