import pygame
from frog import Frog
from obstacle import Obstacle
from network import Network
import time
import os

class GameController:
    def __init__(self, width, height, fps):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps
        self.WHITE = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("lefrog")
        self.clock = pygame.time.Clock()
        self.lefrog = Frog(self.WIDTH // 4, self.HEIGHT // 2)
        self.obst = Obstacle(350, 440)
        self.running = True
        self.game_over = False
        self.ticks_passed = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = '500,500'

    def handle_events(self, network):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    network.save_weights_biases("w")
                    #self.lefrog.jump()


    def update_game_state(self):
        if(self.lefrog.rect.colliderect(self.obst.rect) or self.lefrog.rect.colliderect(self.obst.rectTop)):
            self.game_over = True
        self.obst.update()
        self.lefrog.update(self.obst)

    def draw(self):
        self.screen.fill(self.WHITE)
        self.lefrog.draw(self.screen)
        self.obst.draw(self.screen)
        pygame.display.flip()

    def run(self, network):
        while self.running:
            self.ticks_passed +=1
            self.clock.tick(self.FPS)
            self.handle_events(network)

            input = network.forward(self.lefrog.getInputs(self.obst))

            #print(input)
            if(input > 0.5):
                self.lefrog.jump()


            self.update_game_state()
            self.draw()
            
            if(self.game_over == True):
                local_fitness = self.lefrog.fitness(self.ticks_passed)
                network.calc_fitness(local_fitness)
                return False
        pygame.quit()

if __name__ == "__main__":
    fps = 80
    game_controller = GameController(370, 500, fps)
    network = Network(4, 60, 1)

    network.load_weights()
    while(game_controller.run(network) == False):
        game_controller = GameController(370, 500, fps)
