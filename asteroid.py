import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from random import uniform


class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = uniform(20, 50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)

            sub_asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
            sub_asteroid_2 = Asteroid(self.position.x, self.position.y, radius)

            sub_asteroid_1.velocity = v1
            sub_asteroid_2.velocity = v2

        self.kill()
