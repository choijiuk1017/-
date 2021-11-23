import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Home Sweet Home!")
basicFont = pygame.font.SysFont(None,30)
Surface = pygame.display.set_mode((500,400),0, 32)
text = basicFont.render('Home Sweet Home!',True,(255,255,255),(128,128,128))
textRect = text.get_rect()
textRect.centerx = Surface.get_rect().centerx
textRect.centery = Surface.get_rect().centery + 70


while True:
    Surface.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
    pygame.draw.polygon(Surface,(128,128,128),((250, 90), (160,150), (340,150)))
    pygame.draw.polygon(Surface,(255,255,0),((136, 115), (140, 102), (143, 115), (157,114), (145, 121), (150, 134), (140, 126), (129, 134), (134, 121), (122, 114)))
    pygame.draw.polygon(Surface,(255,255,0),((206, 55), (210, 42), (213, 55), (227,54), (215, 61), (220, 74), (210, 66), (199, 74), (204, 61), (192, 54)))
    pygame.draw.polygon(Surface,(255,255,0),((286, 55), (290, 42), (293, 55), (307,54), (295, 61), (300, 74), (290, 66), (279, 74), (284, 61), (272, 54)))
    pygame.draw.polygon(Surface,(255,255,0),((356, 115), (360, 102), (363, 115), (377,114), (365, 121), (370, 134), (360, 126), (349, 134), (354, 121), (342, 114)))
    pygame.draw.rect(Surface,(128,128,128),(175,150,150,100))
    pygame.draw.rect(Surface,(255,255,255),(235,200,30,50))

    Surface.blit(text,textRect)





    pygame.display.update()
