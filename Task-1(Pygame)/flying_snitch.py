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

    #TODO: Make the golden snitch fly using WASD keys

    screen.fill((0, 0, 0))  # clear screen
    
    pg.draw.circle(screen, (255, 223, 0), (x, y), radius)  

    pg.draw.line(screen, (255, 255, 255), (x - radius*2, y), (x - radius*4, y - 10), 3)
    pg.draw.line(screen, (255, 255, 255), (x + radius*2, y), (x + radius*4, y - 10), 3)

    pg.display.flip()

pg.quit()
