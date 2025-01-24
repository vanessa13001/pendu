import pygame

pygame.init()

screen_width = 1080
screen_height = 720
screen_size=(screen_width,screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First attempt")

width = 5
height = 5

vel = 20
padding = 5

x = screen_width/2 - width # x position of object 
y = screen_height/2 - height - padding # y position of object

is_jump = False
jump_count = 10

def redraw_game_window():
    screen.fill((255,255,255)) # background color of game window 
    # screen.blit('background.png', (position-x, position-y)) # put a background picture instead of coloir
    pygame.draw.rect(screen, (187,133,136), (x, y, width, height)) # size of the screen, color of object, position x and y + surface of object)
    pygame.display.update()

run = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
    
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and x > vel:
        x -= vel

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < screen_width - width - vel:
        x += vel
    
    if not is_jump:
        if (keys[pygame.K_UP] or keys[pygame.K_z]) and y > 0 + vel :
            y -= vel

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < screen_height - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            negative = 1

            if jump_count < 0:
                negative = -1

            y -= (jump_count ** 2) *0.5 * negative
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    
    redraw_game_window()




pygame.quit() # close the windows