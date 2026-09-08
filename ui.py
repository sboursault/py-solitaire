import functools
from typing import NamedTuple

import pygame
from pygame import Surface, Rect

# TODO move to sol
class Card(NamedTuple):
    value: str
    rect: Rect
    is_face_up: bool


pygame.init()

SPACE_WITHIN_COL = 30

# GAME_FONT = pygame.freetype.Font("your_font.ttf", 24)
GAME_FONT = pygame.freetype.SysFont('DejaVu Sans', 30)


@functools.cache
def get_bg_img():
    img = pygame.image.load('/home/seb/Images/Pokemon/assets/images/0249.png').convert_alpha()
    return pygame.transform.smoothscale(img, (700, 700))


def draw_bg(screen: Surface):
    screen.fill("cadetblue2")
    # screen.fill("darkgreen")
    image = get_bg_img()
    left = (screen.get_width() - image.get_width()) / 2
    top = (screen.get_height() - image.get_height()) / 2
    screen.blit(image, (left, top))


def render_stack(stack: dict, pos: tuple[int, int]) -> list[Card]:
    count = 0
    cards: list[Card] = []
    for card in stack['face_down']:
        cards.append(card_rect(card, (pos[0], pos[1] + SPACE_WITHIN_COL * count), True))
        count = count + 1
    for card in stack['face_up']:
        cards.append(card_rect(card, (pos[0], pos[1] + SPACE_WITHIN_COL * count), False))
        count = count + 1

    return cards


def card_rect(value: str, pos: tuple[int, int], face_down=False) -> Card:
    return Card(value, pygame.Rect(pos[0], pos[1], 100, 200), not face_down)


def render_card(screen: Surface, card: Card,
                card_focused: str | None = None) -> Card:
    border_color = 'red' if card_focused == card.value else 'black'
    if card.is_face_up:
        pygame.draw.rect(screen, "white", card.rect)
        pygame.draw.rect(screen, border_color, card.rect, 3)
        color = 'red' if card[0][0] in ['♦', '♥'] else 'black'
        GAME_FONT.render_to(screen, (card.rect[0] + 5, card.rect[1] + 5), card.value, color)
    else:
        pygame.draw.rect(screen, "blue", card.rect)
        pygame.draw.rect(screen, border_color, card.rect, 3)
    return card
