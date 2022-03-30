import pygame
from pygame.locals import *
from bird import Bird
from ground import Ground

clock = pygame.time.Clock()
GAME_SPEED = 10
SCREEN_SIZE = (400, 800)
GROUND_SIZE = (2*SCREEN_SIZE[0], 100)
GRAVITY = 1

def is_off_screen(sprite):
        return sprite.rect[0] < -(sprite.rect[2])

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

BACKGROUND = pygame.image.load('sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, SCREEN_SIZE)

#creating the bird
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

#creating the ground
ground_group = pygame.sprite.Group()
ground = (Ground(GROUND_SIZE, SCREEN_SIZE[1], 2*i*SCREEN_SIZE[0]) for i in range(2))
ground_group.add(ground)

while 1:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0,0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove()
        new_ground = Ground(GROUND_SIZE, SCREEN_SIZE[1], 2*SCREEN_SIZE[0])
        ground_group.add(new_ground)

    bird_group.update()
    ground_group.update()
    bird_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update()
