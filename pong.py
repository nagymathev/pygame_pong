import pygame
from sys import exit

pygame.init()

screen_dims = (800, 600)
screen = pygame.display.set_mode(screen_dims)
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
default_font = pygame.font.Font(None, 50)

# Background
background_dims = (screen_dims)
background_surf = pygame.Surface(background_dims)
background_surf.fill("black")

# Blue Player (Left)
blue_dims = (15, 125)
blue_surf = pygame.Surface(blue_dims)
blue_surf.fill("blue")
blue_rect = blue_surf.get_rect(center = (50, 300))

blue_speed = 4
blue_points = 0

# Red Player (Right)
red_dims = (15, 125)
red_surf = pygame.Surface(red_dims)
red_surf.fill("red")
red_rect = red_surf.get_rect(center = (750, 300))

red_speed = 4
red_points = 0

# Ball
ball_dims = (20, 20)
ball_surf = pygame.Surface(ball_dims)
ball_surf.fill("white")
ball_rect = ball_surf.get_rect(center = (screen_dims[0] / 2, screen_dims[1] / 2))

ball_vel_x = 2
ball_vel_y = 1


while True:
    screen.blit(background_surf, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        blue_rect.y += blue_speed
    if keys[pygame.K_w]:
        blue_rect.y -= blue_speed
    if keys[pygame.K_UP]:
        red_rect.y -= red_speed
    if keys[pygame.K_DOWN]:
        red_rect.y += red_speed

    ball_rect.x += ball_vel_x
    ball_rect.y += ball_vel_y

    if ball_rect.colliderect(blue_rect) or ball_rect.colliderect(red_rect):
        if ball_vel_x < 0:
            ball_vel_x -= 1
        if ball_vel_x > 0:
            ball_vel_x += 1
        if ball_vel_y < 0:
            ball_vel_y -= 1.2
        if ball_vel_y > 0:
            ball_vel_y += 1.2

        ball_vel_x *= -1

    if ball_rect.bottom >= screen_dims[1] or ball_rect.top <= 0:
        ball_vel_y *= -1

    if ball_rect.left <= 0:
        red_points += 1
        ball_vel_x = -2
        ball_vel_y = -1
        ball_rect.center = (screen_dims[0] / 2, screen_dims[1] / 2)

    if ball_rect.right >= screen_dims[0]:
        blue_points += 1
        ball_vel_x = 2
        ball_vel_y = 1
        ball_rect.center = (screen_dims[0] / 2, screen_dims[1] / 2)

    blue_score_surf = default_font.render(f"Score: {blue_points}", True, "blue")
    blue_score_reft = blue_score_surf.get_rect(center = (200, 50))
    screen.blit(blue_score_surf, blue_score_reft)

    red_score_surf = default_font.render(f"Score: {red_points}", True, "red")
    red_score_reft = red_score_surf.get_rect(center = (600, 50))
    screen.blit(red_score_surf, red_score_reft)

    screen.blit(blue_surf, blue_rect)
    screen.blit(red_surf, red_rect)
    screen.blit(ball_surf, ball_rect)

    pygame.display.update()
    clock.tick(60)