import pygame
from pygame.locals import *



class Bird(pygame.sprite.Sprite):

    def __init__(self, screen_size = (400, 800), speed = 10):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('sprites/yellowbird-upflap.png').convert_alpha(),
                       pygame.image.load('sprites/yellowbird-midflap.png').convert_alpha(),
                       pygame.image.load('sprites/yellowbird-downflap.png').convert_alpha()
        ]

        self.speed = speed

        self.current_image = 0

        self.image = pygame.image.load('sprites/yellowbird-upflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect[0], self.rect[1] = screen_size[0]/2, screen_size[1]/2

    def update(self, gravity = 1):
        self.current_image = (self.current_image + 1)%3
        self.image = self.images[self.current_image]
        self.speed += gravity

        #update height
        self.rect[1] += self.speed

    def bump(self, speed = 10):
        self.speed = -speed