import random
import pygame

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

Sid = Actor('bird1', (75, 350))


gap = 140
top_pipe = Actor('top', (300, 0))
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))
scroll_speed = -0.-10
gravity = 0.3
Sid.score = 0

def on_mouse_down():
    if Sid.alive:
        Sid.speed = -6.5

def draw():
    screen.blit('background', (0, 0))
    Sid.draw()
    top_pipe.draw()
    bottom_pipe.draw()

    screen.draw.text(
                        str(Sid.score),
                        color='white',
                        midtop = (20, 10),
                        fontsize = 30,
                    )

def update():
    Sid.speed = Sid.speed + gravity
    Sid.y = Sid.y + Sid.speed
    top_pipe.x = top_pipe.x + scroll_speed
    bottom_pipe.x = bottom_pipe.x + scroll_speed

    if top_pipe.right <0:
        top_pipe.midleft = (WIDTH, random.randint (-170, -60))
        bottom_pipe.midleft = (WIDTH, random.randint(-150, -50) + top_pipe.height + gap)
        top_pipe.pair_number = top_pipe.pair_number + 1

    if Sid.y > HEIGHT:
        reset()

    if (Sid.colliderect(top_pipe) or Sid.colliderect(bottom_pipe)):
        hit_pipe()

    if Sid.alive:
        if Sid.speed > 0:
            Sid.image = 'bird1'
        else:
            Sid.image = 'bird0'

    if top_pipe.right < Sid.x:
        Sid.score = top_pipe.pair_number

    if keyboard.f:
        pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()


def reset():
    Sid.speed = 1
    Sid.center = (75, 350)
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    Sid.image = 'bird1'
    Sid.alive = True
    top_pipe.pair_number = 1
    Sid.score = 0

def hit_pipe():
    Sid.image = 'birddead'
    Sid.alive = False

reset()
