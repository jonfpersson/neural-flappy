import pygame
import math
import random

class Frog:
    def __init__(self, x, y):
        self.score = 0
        self.score_flag = False

        self.x = x + random.uniform(-0.5, 0.5)
        self.y = y + random.uniform(-0.5, 0.5)
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8
        self.image = pygame.transform.scale(pygame.image.load('leFrog.png'), (60, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, obst):
        if(self.y > 480 or self.y < 10):
            return
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.center = (self.x, self.y)
        
        # Add point when lefrog passes the obstacle
        if(self.x > obst.x ):
            if(self.score_flag == False):
                self.score += 1
                #print(self.score)
                self.score_flag = True
        else:
            self.score_flag = False


    def jump(self):
        self.velocity = self.jump_strength

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def fitness(self, seconds):
        return  seconds + self.score
    
    def getInputs(self, obst):
        bottom_middle_x = obst.rect.centerx
        bottom_middle_y = obst.rect.bottom
        
        top_middle_x = obst.rectTop.centerx
        top_middle_y = obst.rectTop.bottom
        
        distanceToBottom = math.sqrt(bottom_middle_x*bottom_middle_x + bottom_middle_y*bottom_middle_y)
        distanceToTop = math.sqrt(top_middle_x*top_middle_x + top_middle_y*top_middle_y)
        return [self.y, distanceToBottom, distanceToTop, self.score_flag]
