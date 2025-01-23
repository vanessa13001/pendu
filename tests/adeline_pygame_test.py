import pygame

pygame.init()

screen_size=(1080,720)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First attempt")

x = 50 # x position of object 
y = 50 # y position of object
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        x -= vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_UP] or keys[pygame.K_z]:
        y -= vel

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
    

    screen.fill((255,255,255))
    pygame.draw.rect(screen, (187,133,136), (x, y, width, height)) # size of the screen, color of object, position x and y + surface of object)
    pygame.display.update()


pygame.quit() # close the windows