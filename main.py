# Example file showing a circle moving on screen
# https://www.pygame.org/docs/


# https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect


import pygame
import pygame.freetype  # Import the freetype module.
from pygame import Rect

from sol import *
import ui
from ui import render_stack

COL_WIDTH = 190

COL_TOP = 220

stacks = deal_cards()


def main() -> None:
    # pygame setup
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    rects: list[tuple[str, Rect]] = []

    card_focused: str | None = None

    while running:

        card_clicked: str | None = None

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

        if is_face_down(stacks, card_clicked):
            return_card(stacks, card_clicked)
        elif is_face_up(stacks, card_clicked):
            if not card_focused:
                card_focused = card_clicked
            else:
                if card_focused == card_clicked:
                    card_focused = None
                # else:
                # move cards

        # fill the screen with a color to wipe away anything from last frame
        ui.draw_bg(screen)

        # rects.append(render_card(screen, '♠25', (290, 5), face_down=True))
        # rects.append(render_card(screen, '♠25', (290 + COL_WIDTH, 5), face_down=True))
        # rects.append(render_card(screen, '♠25', (290 + COL_WIDTH * 2, 5), face_down=True))
        # rects.append(render_card(screen, '♠25', (290 + COL_WIDTH * 3, 5), face_down=True))

        count = 0
        for stack in stacks:
            rects = rects + render_stack(screen, stack, (5 + COL_WIDTH * count, COL_TOP), card_focused)
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
