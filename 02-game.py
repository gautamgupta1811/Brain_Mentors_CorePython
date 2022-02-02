import pygame
import random
pygame.init()


def score(count):
    font = pygame.font.SysFont("Seogoe UI", 30)
    text = font.render(f"Score: {count}", False, black)
    screen.blit(text, (30, 30))


def game_over():
    font = pygame.font.SysFont("Seogoe UI", 50)
    text = font.render(f"GAME OVER", False, black)
    screen.blit(text, (width//2-40, height//2))

def life_count(life):
    font = pygame.font.SysFont("Seogoe UI", 30)
    text = font.render(f"Life Remaning: {life}", False, black)
    screen.blit(text, (width - 200, 30))

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Keepie Uppie")

red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
white = 255, 255, 255
black = 0, 0, 0

ball_x, ball_y = width//2, height
radius = 20
life = 3
flag = False
count = 0
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
            flag = True
            ball_y -= 100
            if life > 0:
                count += 1
            ball_x = random.randint(ball_x-125, ball_x+125)
            if ball_x > width - radius:
                ball_x = width - radius
            elif ball_x < radius:
                ball_x = radius

    if ball_y <= height:
        ball_y += 1
    if ball_y >= height and flag:
        if life > 0:
            life -= 1
        flag = False
        print(life)
    if life <= 0:
        game_over()
        ball_x, ball_y = width//2, height
    life_count(life)
    score(count)
    pygame.display.update()



# score
# game over
# life
# speed of game