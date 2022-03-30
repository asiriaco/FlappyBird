import pygame

class Ground(pygame.sprite.Sprite):

    def __init__(self, screen_size, height, xpos):

        height = height - screen_size[1]

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('sprites/base.png')
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = height

    def update(self, game_speed=10):

        self.rect[0] -= game_speed
