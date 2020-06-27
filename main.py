import pygame
import time
from os import listdir
# from os.path import isfile, join

pygame.init()

SCREEN_X = 150
SCREEN_Y = 150
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

SPRT_start_X = 0
SPRT_start_Y = 0

SPRT_end_X = 150
SPRT_end_Y = 150

mydir = 'C:\\Users\\taehw\\Documents\\helltaker-animation-icon\\devils'
devils = [f for f in listdir(mydir) if f[-4:] == '.png']

pygame.display.set_caption('Cute Luciper!')
background = pygame.image.load('background.png')
sprite_idx = devils.index('Lucifer.png')
sprite = pygame.image.load(f'{mydir}\\{devils[sprite_idx]}')
# sprite = pygame.image.load(f'{mydir}\\Azazel.png')

shut_down = False
frame = True
while not shut_down:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shut_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                shut_down = True
            if event.key == pygame.K_RIGHT:
                sprite_idx = sprite_idx + 1 if sprite_idx + \
                    1 <= len(devils) - 1 else 0
                sprite = pygame.image.load(f'{mydir}\\{devils[sprite_idx]}')
            if event.key == pygame.K_LEFT:
                sprite_idx = sprite_idx - \
                    1 if sprite_idx >= 1 else len(devils) - 1
                sprite = pygame.image.load(f'{mydir}\\{devils[sprite_idx]}')

        if event.type == pygame.MOUSEBUTTONUP:
            if frame:
                screen = pygame.display.set_mode(
                    (SCREEN_X, SCREEN_Y), pygame.NOFRAME)
            else:
                screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
            frame = not frame

    sprite.set_clip(pygame.Rect(
        SPRT_start_X, SPRT_start_Y, SPRT_end_X, SPRT_end_Y))
    sprite_cut = sprite.subsurface(sprite.get_clip())

    screen.blit(background, (0, 0))
    screen.blit(sprite_cut, (0, 0))
    pygame.display.update()

    SPRT_start_X = SPRT_start_X + 150 if SPRT_start_X + 150 <= 1650 else 0
    SPRT_end_X = SPRT_end_X + 150 if SPRT_end_X + 150 <= 1800 else 150

    time.sleep(0.055)

pygame.quit()
