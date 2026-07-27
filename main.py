# Example file showing a circle moving on screen
from typing import Tuple

import pygame
import pygame.freetype  # Import the freetype module.
from pygame import Surface, SurfaceType

pygame.init()

# GAME_FONT = pygame.freetype.Font("your_font.ttf", 24)
GAME_FONT = pygame.freetype.SysFont('DejaVu Sans', 30)

COL_TOP = 220
COL_WIDTH = 190
SPACE_WITHIN_COL = 30


def render_stack(screen: Surface, stack: dict, pos: tuple[int, int]):
    count = 0
    for card in stack['face_down']:
        render_card(screen, card, (pos[0], pos[1] + SPACE_WITHIN_COL * count), face_down=True)
        count = count + 1
    # render_card(screen, stack['face_down'][0], (pos[0], pos[1] + SPACE_WITHIN_COL * count), face_down=True)
    # count = count + 1
    # render_card(screen, stack['face_down'][1], (pos[0], pos[1] + SPACE_WITHIN_COL * count), face_down=True)
    # count = count + 1
    # render_card(screen, stack['face_down'][2], (pos[0], pos[1] + SPACE_WITHIN_COL * count), face_down=True)
    # count = count + 1
    for card in stack['face_up']:
        render_card(screen, card, (pos[0], pos[1] + SPACE_WITHIN_COL * count))
        count = count + 1
    # render_card(screen, stack['face_up'][0], (pos[0], pos[1] + SPACE_WITHIN_COL * count))
    # count = count + 1
    # render_card(screen, stack['face_up'][1], (pos[0], pos[1] + SPACE_WITHIN_COL * count))
    # count = count + 1
    # render_card(screen, stack['face_up'][2], (pos[0], pos[1] + SPACE_WITHIN_COL * count))


def render_card(screen: Surface, value: str, pos: tuple[int, int], face_down=False):
    if face_down:
        pygame.draw.rect(screen, "blue", (pos, (100, 200)))
        pygame.draw.rect(screen, "black", (pos, (100, 200)), 3)
    else:
        pygame.draw.rect(screen, "white", (pos, (100, 200)))
        pygame.draw.rect(screen, "black", (pos, (100, 200)), 3)
        GAME_FONT.render_to(screen, (pos[0] + 5, pos[1] + 5), value, (0, 0, 0))


def main() -> None:
    # pygame setup
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("darkgreen")

        render_card(screen, '♠1', (290, 5))
        render_card(screen, '♠1', (290 + COL_WIDTH, 5))
        render_card(screen, '♠1', (290 + COL_WIDTH * 2, 5))
        render_card(screen, '♠1', (290 + COL_WIDTH * 3, 5))

        stack = {
            'face_down': [
                '♠1',
                '♠2',
                '♠3',
            ],
            'face_up': [
                '♦8',
                '♠7',
                '♠34',
                '♦8000',
            ],
        }

        # render_card(screen, '♣10', (5, col_top))
        render_stack(screen, stack, (5, COL_TOP))
        render_stack(screen, stack, (5 + COL_WIDTH, COL_TOP))

        #render_card(screen, '♠K', (5 + COL_WIDTH, COL_TOP), face_down=True)
        #render_card(screen, '♠K', (5 + COL_WIDTH * 2, COL_TOP), face_down=True)
        #render_card(screen, '♠K', (5 + COL_WIDTH * 3, COL_TOP), face_down=True)
        #render_card(screen, '♠K', (5 + COL_WIDTH * 4, COL_TOP), face_down=True)
        #render_card(screen, '♠K', (5 + COL_WIDTH * 5, COL_TOP), face_down=True)
        #render_card (screen, '♠K', (5 + COL_WIDTH * 6, COL_TOP), face_down=True)

        #render_card(screen, '♠K', (5 + COL_WIDTH, COL_TOP + SPACE_WITHIN_COL))
        #render_card(screen, '♠K', (5 + COL_WIDTH, COL_TOP + SPACE_WITHIN_COL * 2))

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
