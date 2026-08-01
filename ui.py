import pygame
from pygame import Surface, Rect

pygame.init()

SPACE_WITHIN_COL = 30

# GAME_FONT = pygame.freetype.Font("your_font.ttf", 24)
GAME_FONT = pygame.freetype.SysFont('DejaVu Sans', 30)


def render_stack(screen: Surface, stack: dict, pos: tuple[int, int],
                 card_clicked: str | None = None) -> list[tuple[str, Rect]]:
    count = 0
    rects = []
    for card in stack['face_down']:
        rects.append(render_card(screen, card, (pos[0], pos[1] + SPACE_WITHIN_COL * count), True, card_clicked))
        count = count + 1
    for card in stack['face_up']:
        rects.append(render_card(screen, card, (pos[0], pos[1] + SPACE_WITHIN_COL * count), False, card_clicked))
        count = count + 1
    return rects


def render_card(screen: Surface, value: str, pos: tuple[int, int], face_down=False,
                card_clicked: str | None = None) -> tuple[str, Rect]:
    border_color = 'red' if card_clicked == value else 'black'
    if face_down:
        rect = pygame.draw.rect(screen, "blue", (pos, (100, 200)))
        pygame.draw.rect(screen, border_color, (pos, (100, 200)), 3)
    else:
        rect = pygame.draw.rect(screen, "white", (pos, (100, 200)))
        pygame.draw.rect(screen, border_color, (pos, (100, 200)), 3)
        color = 'red' if value[0] in ['♦', '♥'] else 'black'
        GAME_FONT.render_to(screen, (pos[0] + 5, pos[1] + 5), value, color)
    return value, rect
