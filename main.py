import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food


pygame.init()
win = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")

control = Control()
snake = Snake()
gui = Gui()
food = Food()

gui.initField()
food.getFoodPosition(gui)
speed = 0


while control.flagGame:
    gui.checkVictoryOrLose()
    control.control()
    win.fill((0, 0, 0))
    if gui.game == "PLAYING":
        snake.drawSnake(win)
        food.drawFood(win)
        gui.drawLevle(win)
        gui.drawIndicater(win)
    elif gui.game == "VICTORY":
        gui.drawVictory(win)
    elif gui.game == "LOSE":
        gui.drawLose(win)

    if speed % 20 == 0 and control.flagPause and gui.game == "PLAYING":
        snake.move(control)
        snake.checkCrash(gui)
        snake.eat(food, gui)
        snake.checkEndWin()
        snake.animation()
    speed += 1
    pygame.display.flip()
