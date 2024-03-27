import pygame
pygame.init()

screen = pygame.display.set_mode((700,400))
pygame.display.set_caption("Ball Game")
loop = True

#coordinates of the center
x = 350
y = 200
#borders
up_limit = 25
down_limit = 375
left_limit = 25
right_limit = 675

clock = pygame.time.Clock()

while loop:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    #checking if the arrow buttons are pressed and if the ball's center is leaving the borders
    if pressed[pygame.K_UP] and y >= up_limit:
        y -= 20
        y = max(y, up_limit)
    if pressed[pygame.K_DOWN] and y < down_limit:
        y += 20
        y = min(y, down_limit)
    if pressed[pygame.K_LEFT] and x > left_limit:
        x -= 20
        x = max(x, left_limit)
    if pressed[pygame.K_RIGHT] and x < right_limit:
        x += 20
        x = min(x, right_limit)

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,255,0), (x,y), radius=25)

    pygame.display.flip()
    clock.tick(60)