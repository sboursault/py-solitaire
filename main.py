# Example file showing a circle moving on screen
# https://www.pygame.org/docs/


# https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect


import pygame
import pygame.freetype  # Import the freetype module.
from pygame import Rect

from sol import *
import ui
from ui import render_stack, Card, render_card

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

    cards: list[Card] = []

    card_focused: Card | None = None
    card_dragged: Card | None = None
    drag_cursor_start: tuple[int, int] | None = None
    drag_origin_rect: tuple[int, int, int, int] | None = None


    while running:

        card_clicked: Card | None = None

        count = 0
        for stack in stacks:
            cards = cards + render_stack(stack, (5 + COL_WIDTH * count, COL_TOP))
            count = count + 1

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                card_dragged = find_clicked_card(cards)
                drag_cursor_start = pygame.mouse.get_pos()
                drag_origin_rect = card_dragged.rect
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if card_dragged:
                    offset = (mouse_pos[0] - drag_cursor_start[0], mouse_pos[1] - drag_cursor_start[1])
                    card_dragged.rect = pygame.Rect(drag_origin_rect[0] + offset[0],
                                                    drag_origin_rect[1] + offset[1],
                                                    drag_origin_rect[2],
                                                    drag_origin_rect[3])
                    # card_dragged.topleft = event.pos + offset
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if card_dragged:
                    print(pygame.mouse.get_pos())
                    print(drag_cursor_start)
                    if pygame.mouse.get_pos() == drag_cursor_start:
                        print('hello')
                        card_clicked = card_dragged
                    else:
                        print('zut')
                        card_dragged.rect = drag_origin_rect
                    card_dragged = None

        if card_clicked:
            if not card_clicked.is_face_up:
                return_card(stacks, card_clicked.value)
            else:
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

        for card in cards:
            render_card(screen, card, card_focused)

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


def find_clicked_card(cards: list[Card]) -> Card | None:
    click_pos = pygame.mouse.get_pos()
    match = None
    for card in cards:
        if card.rect.collidepoint(click_pos):
            match = card
    return match


if __name__ == '__main__':
    main()
