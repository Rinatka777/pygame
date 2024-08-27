import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
        # we will be using this later
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        def draw(self, screen):
        # Call pygame.draw.polygon
            pygame.draw.polygon(
            screen,               # The screen object to draw on
            (255, 255, 255),      # Color: white (RGB)
            self.triangle(),      # Points list (use self.triangle())
            2                     # Line width: 2
        )
        

    def update(self, dt):
        # sub-classes must override
        pass
