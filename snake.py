import pygame

class Snake:
    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move(self, control):
        speed = 11
        if control.flagDirection == "RIGHT":
            self.head[0] += speed
        elif control.flagDirection == "LEFT":
            self.head[0] -= speed
        elif control.flagDirection == "UP":
            self.head[1] -= speed
        elif control.flagDirection == "DOWN":
            self.head[1] += speed

    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def drawSnake(self, win):
        for seg in self.body:
            pygame.draw.rect(win, (255, 255, 255), (seg[0], seg[1], 10, 10))

    def checkEndWin(self):
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        if self.head == food.foodPosition:
            self.body.append(food.foodPosition)
            food.getFoodPosition(gui)
            gui.getNewIndicater()


    def checkCrash(self, gui):
        if self.head in gui.barrier:
            self.body.pop()
            gui.indicater.pop()
        if self.head in self.body[1:]:
            self.body.pop()
            gui.indicater.pop()
