import pygame

white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Circle")
done = True

x = 50
y = 50

clock = pygame.time.Clock()

while done:

    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - 20 - 25 >= 0:
            y -= 20
        if pressed[pygame.K_DOWN] and y + 20 + 25 <= 300:
            y += 20
        if pressed[pygame.K_LEFT] and x - 20 - 25 >= 0:
            x -= 20
        if pressed[pygame.K_RIGHT] and x + 20 + 25 <= 300:
            x += 20

    pygame.draw.circle(screen, red, (x,y), 25)

    pygame.display.flip()
    clock.tick(60)
