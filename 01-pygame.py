import pygame
from pygame.locals import *
# starts the pygame module
pygame.init()

# initialize a screen
screen = pygame.display.set_mode((1000, 500))

# change caption/title
pygame.display.set_caption("My game")

# load any image in pygame
ball = pygame.image.load("ball.png")

# set icon of pygame window
pygame.display.set_icon(ball)

# colors

red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
white = 255, 255, 255
black = 0, 0, 0
x, y = 20, 40
while True:
    screen.fill(white)
    rect = pygame.draw.rect(screen, red, [x, y, 40, 50])
    circle = pygame.draw.circle(screen, green, [50, 50], 30)
    # closing of game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            x = x + 10

    pygame.display.update()
