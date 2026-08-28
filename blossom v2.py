import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (5,5,10)
CENTER = (WIDTH//2, HEIGHT//2)

flowers = []


class Bloom:

    def __init__(self):
        self.radius = 0
        self.rotation = random.uniform(0, 360)

        self.color = random.choice([
            (0,180,255),
            (150,80,255),
            (255,120,220),
            (120,255,255)
        ])

    def update(self):

        self.radius += 0.8
        self.rotation += 0.3

    def draw(self):

        for layer in range(4):

            for p in range (12):

                pts = []

                off = math.radians(
                    p*30 + self.rotation + layer * 8
                )

                for i in range(180):

                    t=math.radians(i)

                    r=(self.radius + layer * 15) * abs(math.sin(4 * t)
                    )

                    x=CENTER[0] + r * math.cos(t + off)
                    y=CENTER[1] + r * math.sin(t + off)

                    pts.append((x,y))

                if len(pts)>2:

                    pygame.draw.lines(
                        screen,
                        self.color,
                        False,
                        pts,
                        2
                    )

            pygame.draw.circle(
                screen,
                (255,255,255),
                CENTER,
                4
            )

flowers.append(Bloom())

frame = 0
running = True

while running:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    frame += 1

    if frame % 150 == 0:
        flowers.append(Bloom())

    for f in flowers[:]:
        f.update()
        f.draw()
        if f.radius > 200:
            flowers.remove(f)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
