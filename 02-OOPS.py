import pygame
import random
pygame.init()


width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
# class variables --> data member
# class functions --> member function
class Circle:
    def __init__(self):
        self.radius = random.randint(10, 50)
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.move_x = random.randint(-3, 3)
        self.move_y = random.randint(-3, 3)

    def update(self):
        if self.x > width - self.radius:
            self.move_x = random.randint(-3, 0)
        elif self.x < self.radius:
            self.move_x = random.randint(0, 3)
        self.x += self.move_x
        if self.y > height - self.radius:
            self.move_y = random.randint(-3, 0)
        elif self.y < self.radius:
            self.move_y = random.randint(0, 3)
        self.y += self.move_y

# 20 circles
circle_list = []
num = int(input("Enter number of circle: "))
for i in range(num):
    circle = Circle()
    circle_list.append(circle)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for i in range(num):
        pygame.draw.circle(screen, circle_list[i].color, [circle_list[i].x, circle_list[i].y], circle_list[i].radius)
        circle_list[i].update()
    pygame.display.update()

## access modifiers --> private, public, protected