import pygame
from pygame.locals import *


def draw_rect(s, x, y, c,p_size):
    pygame.draw.rect(s, c, Rect(x - (p_size/2), y - (p_size/2), p_size, p_size), 5)
