import pygame
import time

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
play_and_pause = True
while not shut_down:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shut_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            play_and_pause = not play_and_pause

    lucifer.set_clip(pygame.Rect(
        SPRT_start_X, SPRT_start_Y, SPRT_end_X, SPRT_end_Y))
    lucifer_pic = lucifer.subsurface(lucifer.get_clip())

    screen.blit(background, (0, 0))
    screen.blit(lucifer_pic, (0, 0))
    pygame.display.update()

    if play_and_pause:
        SPRT_start_X = SPRT_start_X + 150 if SPRT_start_X + 150 <= 1650 else 0
        SPRT_end_X = SPRT_end_X + 150 if SPRT_end_X + 150 <= 1800 else 150

    time.sleep(0.05)

pygame.quit()
