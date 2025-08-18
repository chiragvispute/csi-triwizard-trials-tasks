import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Flying Snitch")

x, y = 100, 100
speed = 1
radius = 15

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and y - speed > radius:
        y -= speed
    if keys[pg.K_s] and y + speed < 600 - radius:
        y += speed
    if keys[pg.K_a] and x - speed > radius:
        x -= speed
    if keys[pg.K_d] and x + speed < 800 - radius:
        x += speed

    screen.fill((0, 0, 0))  # clear screen
    
    # Draw the golden snitch
    pg.draw.circle(screen, (255, 223, 0), (x, y), radius)  # golden ball
    pg.draw.line(screen, (255, 255, 255), (x - radius*2, y), (x - radius*4, y - 10), 3)  # left wing
    pg.draw.line(screen, (255, 255, 255), (x + radius*2, y), (x + radius*4, y - 10), 3)  # right wing

    pg.display.flip()  # refresh screen

pg.quit()
