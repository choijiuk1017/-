import pygame, sys, time
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# Set up direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the box data structure.
c1 = {'circle':pygame.Rect((300, 80), (25, 25)), 'color':RED, 'dir':UPRIGHT}
c2 = {'circle':pygame.Rect((200, 100), (10, 10)), 'color':GREEN, 'dir':UPLEFT}
c3 = {'circle':pygame.Rect((100, 150), (50, 50)), 'color':BLUE, 'dir':DOWNLEFT}
circles = [c1, c2, c3]

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    for c in circles:
        # Move the box data structure.
        if c['dir'] == DOWNLEFT:
            c['circle'].left -= MOVESPEED
            c['circle'].top += MOVESPEED
        if c['dir'] == DOWNRIGHT:
            c['circle'].left += MOVESPEED
            c['circle'].top += MOVESPEED
        if c['dir'] == UPLEFT:
            c['circle'].left -= MOVESPEED
            c['circle'].top -= MOVESPEED
        if c['dir'] == UPRIGHT:
            c['circle'].left += MOVESPEED
            c['circle'].top -= MOVESPEED

        # Check whether the box has moved out of the window.
        if c['circle'].top < 0:
            # The box has moved past the top.
            if c['dir'] == UPLEFT:
                c['dir'] = DOWNLEFT
            if c['dir'] == UPRIGHT:
                c['dir'] = DOWNRIGHT
        if c['circle'].bottom > WINDOWHEIGHT:
            # The box has moved past the bottom.
            if c['dir'] == DOWNLEFT:
                c['dir'] = UPLEFT
            if c['dir'] == DOWNRIGHT:
                c['dir'] = UPRIGHT
        if c['circle'].left < 0:
            # The box has moved past the left side.
            if c['dir'] == DOWNLEFT:
                c['dir'] = DOWNRIGHT
            if c['dir'] == UPLEFT:
                c['dir'] = UPRIGHT
        if c['circle'].right > WINDOWWIDTH:
            # The box has moved past the right side.
            if c['dir'] == DOWNRIGHT:
                c['dir'] = DOWNLEFT
            if c['dir'] == UPRIGHT:
                c['dir'] = UPLEFT

        # Draw the box onto the surface.
        pygame.draw.ellipse(windowSurface, c['color'], c['circle'])

    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)
