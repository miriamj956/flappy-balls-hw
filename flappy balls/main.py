import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Flappy Balls"

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)

CLR = (R,G,B)
GRAVITY = 2000.0

class Balls():
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = random.randint(150,250)
        self.vy = 0
        self.radius = 40

    def drawBall(self):
        #pos(self.x, self.y)
        screen.draw.filled_circle((self.x, self.y), self.radius, CLR)

balls = [Balls(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(5)]

def draw():
    screen.clear()
    screen.fill(color = "grey")
    for ball in balls:
        ball.drawBall()

def update(dt):
    for ball in balls:
        uy = ball.vy
        ball.vy = ball.vy + (GRAVITY * dt)
        ball.y += (uy + ball.vy) * 0.5 * dt

        if ball.y > HEIGHT:
            ball.y = HEIGHT - ball.radius
            ball.vy = -ball.vy * 0.9

        ball.x += ball.vx * dt
        if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
            ball.vx = -ball.vx

def on_key_down(key):
    if key == keys.UP:
        for ball in balls:
            ball.vy = -500



pgzrun.go()