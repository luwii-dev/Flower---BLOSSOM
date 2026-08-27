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
        self.age = 0
        self.lifetime = random.randint(360, 540)

        self.color = random.choice([
            (0,180,255),
            (150,80,255),
            (255,120,220),
            (120,255,255)

        ])

    def update(self):
        self.age += 1
        self.radius = min(self.age * 0.9, 220)
        self.rotation += 0.3

    def draw(self):
        fade = max(0, 1 - max(0, self.age - 360) / 180)
        shade = tuple(int(channel * fade) for channel in self.color)

        for layer in range(4):
            points = []
            layer_radius = self.radius - layer * 12

            if layer_radius <= 0:
                continue

            for step in range(181):
                angle = math.radians(step * 2)
                petal_radius = layer_radius * abs(math.sin(4 * angle))
                rotated_angle = angle + math.radians(self.rotation + layer * 8)
                x = CENTER[0] + petal_radius * math.cos(rotated_angle)
                y = CENTER[1] + petal_radius * math.sin(rotated_angle)
                points.append((int(x), int(y)))

            pygame.draw.lines(screen, shade, False, points, 2)

        pygame.draw.circle(
            screen,
            (255,255,255),
            CENTER,
            4
        )

flowers.append(Bloom())

frame=0

running=True

while running:

    for e in pygame.event.get():

        if e.type==pygame.QUIT:
            running=False

    screen.fill(BLACK)

    frame+=1 

    if frame%150==0:
        flowers.append(Bloom())

    for f in flowers[:]:
        f.update()
        f.draw()
        if f.age >= f.lifetime:
            flowers.remove(f)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()