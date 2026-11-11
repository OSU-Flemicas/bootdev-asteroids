import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white",  self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius > ASTEROID_MIN_RADIUS):
            log_event("asteroid_split")

            randAngle = random.uniform(20, 50)

            vector1 = pygame.Vector2(0, 1)
            rotated_vector1 = vector1.rotate(randAngle)

            vector2 = pygame.Vector2(0, 1)
            rotated_vector2 = vector2.rotate(-randAngle)

            newRadius = self.radius - ASTEROID_MIN_RADIUS

            newAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            newAsteroid1.velocity = rotated_vector1 * 102

            newAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            newAsteroid2.velocity = rotated_vector2 * 102
