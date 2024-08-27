# player.py
import pygame
# Import the CircleShape class from CircleShape.py
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        radius = PLAYER_RADIUS  # Define the radius here
        # Call the parent class's constructor
        super().__init__(x, y, radius)

        # Create a field called position: a pygame.Vector2 using the x and y parameters
        self.position = pygame.Vector2(x, y)

        # Create a field called rotation, initialized to 0
        self.rotation = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
