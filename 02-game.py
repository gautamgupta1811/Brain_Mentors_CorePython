import pygame
import random
pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Keepie Uppie")

red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
white = 255, 255, 255

ball_x, ball_y = width//2, height
radius = 20

while True:
    screen.fill(white)
    circle = pygame.draw.circle(screen, green, (ball_x, ball_y - radius), 20)
    mos_x, mos_y = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mos_x, mos_y, 10, 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if circle.colliderect(mouse_rect):
            print("Collision Detected")
            ball_y -= 20
            ball_x = random.randint(0, width)
    if ball_y <= height:
        ball_y += 1
    pygame.display.update()


# ball movement
# score
# game over
# life
# speed of game