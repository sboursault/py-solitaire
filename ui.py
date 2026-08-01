import pygame
from pygame import Surface

pygame.init()

SPACE_WITHIN_COL = 30

# GAME_FONT = pygame.freetype.Font("your_font.ttf", 24)
GAME_FONT = pygame.freetype.SysFont('DejaVu Sans', 30)


def render_stack(screen: Surface, stack: dict, pos: tuple[int, int]):
    count = 0
    for card in stack['face_down']:
        render_card(screen, card, (pos[0], pos[1] + SPACE_WITHIN_COL * count), face_down=True)
        count = count + 1
    for card in stack['face_up']:
        render_card(screen, card, (pos[0], pos[1] + SPACE_WITHIN_COL * count))
        count = count + 1


def render_card(screen: Surface, value: str, pos: tuple[int, int], face_down=False):
    if face_down:
        pygame.draw.rect(screen, "blue", (pos, (100, 200)))
        pygame.draw.rect(screen, "black", (pos, (100, 200)), 3)
    else:
        pygame.draw.rect(screen, "white", (pos, (100, 200)))
        pygame.draw.rect(screen, "black", (pos, (100, 200)), 3)
        color = 'red' if value[0] in ['♦', '♥'] else 'black'
        GAME_FONT.render_to(screen, (pos[0] + 5, pos[1] + 5), value, color)
