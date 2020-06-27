import pygame
import time
from check_OS import your_OS

pygame.init()

SCREEN_X = 150
SCREEN_Y = 150
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

SPRT_start_X = 0
SPRT_start_Y = 0

SPRT_end_X = 150
SPRT_end_Y = 150

pygame.display.set_caption('Cute Luciper!')
background = pygame.image.load('background.png')
lucifer = pygame.image.load('lucifer.png')

shut_down = False
frame = True
while not shut_down:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shut_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            frame = not frame
            if frame:
                screen = pygame.display.set_mode(
                    (SCREEN_X, SCREEN_Y), pygame.NOFRAME)
            else:
                screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

    lucifer.set_clip(pygame.Rect(
        SPRT_start_X, SPRT_start_Y, SPRT_end_X, SPRT_end_Y))
    lucifer_pic = lucifer.subsurface(lucifer.get_clip())

    screen.blit(background, (0, 0))
    screen.blit(lucifer_pic, (0, 0))
    pygame.display.update()

    SPRT_start_X = SPRT_start_X + 150 if SPRT_start_X + 150 <= 1650 else 0
    SPRT_end_X = SPRT_end_X + 150 if SPRT_end_X + 150 <= 1800 else 150

    time.sleep(0.06)

pygame.quit()
