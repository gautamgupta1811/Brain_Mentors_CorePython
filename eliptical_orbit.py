import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 300))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    x_rad = 250
    y_rad = 100

    for degree in range(0, 360, 10):
        x1 = int(math.cos(degree * 2 * math.pi/360) * x_rad) + 300
        y1 = int(math.sin(degree * 2 * math.pi/360) * y_rad) + 150
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 67, 89), [300, 150], 40)
        pygame.draw.ellipse(screen, (255, 255, 255), [50, 50, 500, 200], 1)
        pygame.draw.circle(screen, (0, 255, 255), [x1, y1], 20)
        clock.tick(5)
        pygame.display.update()
