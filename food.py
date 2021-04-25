import pygame
import random

class Food:
    def __init__(self):
        self.foodPosition = []

    def getFoodPosition(self, gui):
        self.foodPosition = random.choice(gui.field)

    def drawFood(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.foodPosition[0], self.foodPosition[1], 10, 10))
