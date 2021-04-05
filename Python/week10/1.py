import pygame
import random
BLACK = (0,0,0)
wHIYE = (255,255,255)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Ball:
    BALL_SIZE = 25

    def_get_random_change(self):
        change = random.random(-2,3)