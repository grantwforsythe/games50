import sys
import pygame
from pathlib import Path

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# RGB colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# create and display the surface object
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set the title for the pygame window
pygame.display.set_caption("Pong")

# create a font object.
file = Path.cwd() / "assets" / "font.ttf"
font = pygame.font.Font(file, 32)

# create a text surface object,
# on which text is drawn on it
text = font.render('Hello, Pong!', True, GREEN, BLUE)

# create a rectangular object for the text surface object
textRect = text.get_rect()

# center the rectangular object.
textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


def main():

    # completely fill the surface object with white color.
    WIN.fill(WHITE)

    # copying the text surface object to the display surface object at the center coordinate
    WIN.blit(text, textRect)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Keypresses 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # draws the surface object to the screen
        pygame.display.update()

    # deactivate the pygame libary
    pygame.quit()
    # exit the program
    sys.exit()

if __name__ == '__main__':
    main()
