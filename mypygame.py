# Example file showing a circle moving on screen
from typing import Tuple

import pygame
import pygame.freetype  # Import the freetype module.
from pygame import Surface, SurfaceType

pygame.init()

# GAME_FONT = pygame.freetype.Font("your_font.ttf", 24)
GAME_FONT = pygame.freetype.SysFont('DejaVu Sans', 30)


def render_card(screen: Surface, value: str, pos: tuple[int, int]):
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

        render_card(screen, '♠K', (240, 160))

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
