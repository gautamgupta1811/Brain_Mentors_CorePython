import pygame

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

while True:
    # closing of game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
