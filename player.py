import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 1)

    def rotate(self, dt, keys):
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED * dt
        elif keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED * dt

    def translate(self, dt, keys):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation)
        if keys[pygame.K_w]:
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= forward * PLAYER_SPEED * dt
        if keys[pygame.K_a]:
            self.position -= right * PLAYER_SPEED * dt
        if keys[pygame.K_d]:
            self.position += right * PLAYER_SPEED * dt

    def update(self, dt):
        self.shoot_timer += dt
        keys = pygame.key.get_pressed()
        self.rotate(dt, keys)
        self.translate(dt, keys)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_timer > PLAYER_SHOOT_COOLDOWN:
            shot = Shot(self.position.x, self.position.y)
            velocity_vector  = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot.velocity = velocity_vector
            self.shoot_timer = 0
