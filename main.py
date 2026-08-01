# Example file showing a circle moving on screen
# https://www.pygame.org/docs/


# https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect

import pygame
import pygame.freetype  # Import the freetype module.
from pygame import Rect

from ui import render_card, render_stack

cards = [
    '♠1',
    '♠2',
    '♠3',
    '♠4',
    '♠5',
    '♠6',
    '♠7',
    '♠8',
    '♠9',
    '♠10',
    '♠J',
    '♠Q',
    '♠K',

    '♥1',
    '♥2',
    '♥4',
    '♥5',
    '♥6',
    '♥7',
    '♥8',
    '♥9',
    '♥10',
    '♥J',
    '♥Q',
    '♥K',

    '♦1',
    '♦2',
    '♦3',
    '♦4',
    '♦5',
    '♦6',
    '♦7',
    '♦8',
    '♦9',
    '♦10',
    '♦J',
    '♦Q',
    '♦K',

    '♣1',
    '♣2',
    '♣3',
    '♣4',
    '♣5',
    '♣6',
    '♣7',
    '♣8',
    '♣9',
    '♣10',
    '♣J',
    '♣Q',
    '♣K',
]

COL_WIDTH = 190

COL_TOP = 220

stacks = [
    {
        'face_down': [
        ],
        'face_up': [
            cards.pop(),
        ],
    },
    {
        'face_down': [
            cards.pop(),
        ],
        'face_up': [
            cards.pop(),
        ],
    },
    {
        'face_down': [
            cards.pop(),
            cards.pop(),
        ],
        'face_up': [
            cards.pop(),
        ],
    },
    {
        'face_down': [
            cards.pop(),
            cards.pop(),
            cards.pop(),
        ],
        'face_up': [
            cards.pop(),
        ],
    },

]


def main() -> None:
    # pygame setup
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    rects: list[tuple[str, Rect]] = []

    card_clicked: str | None = None

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_pos = pygame.mouse.get_pos()
                for rect in rects:
                    if rect[1].collidepoint(click_pos):
                        card_clicked = rect[0]

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("darkgreen")

        rects.append(render_card(screen, '♠1', (290, 5)))
        rects.append(render_card(screen, '♠1', (290 + COL_WIDTH, 5)))
        rects.append(render_card(screen, '♠1', (290 + COL_WIDTH * 2, 5)))
        rects.append(render_card(screen, '♠1', (290 + COL_WIDTH * 3, 5)))

        count = 0
        for stack in stacks:
            rects = rects + render_stack(screen, stack, (5 + COL_WIDTH * count, COL_TOP), card_clicked)
            count = count + 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000


    pygame.quit()


if __name__ == '__main__':
    main()
