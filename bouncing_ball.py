import pygame

pygame.init()

width, height = 800, 400
speed = [1, 1]

background = 255, 255, 255

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ball_rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(background)
    screen.blit(ball, ball_rect)
    pygame.display.update()