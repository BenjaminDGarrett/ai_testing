import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define the size of the screen
screen_width = 800
screen_height = 600

# Create a new window
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the parameters of the moving object
object_width = 50
object_height = 50
object_speed = 100  # pixels per second

# Define a function to draw the object at a given position
def draw_object(x, y):
    # Create a new surface for the object
    object_surface = pygame.Surface((object_width, object_height))

    # Fill the surface with a random color
    object_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    object_surface.fill(object_color)

    # Draw a random pattern on the surface
    for i in range(100):
        pattern_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pattern_x = random.randint(0, object_width)
        pattern_y = random.randint(0, object_height)
        pattern_size = random.randint(5, 20)
        pygame.draw.circle(object_surface, pattern_color, (pattern_x, pattern_y), pattern_size)

    # Draw the surface at the given position
    screen.blit(object_surface, (x, y))

# Define the starting position of the object
object_x = 0
object_y = 0

# Loop forever
while True:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the object at the current position
    draw_object(object_x, object_y)

    # Update the display
    pygame.display.flip()

    # Wait for a short amount of time
    time.sleep(0.1)

    # Move the object to a new position
    object_x += random.randint(-50, 50)
    object_y += random.randint(-50, 50)

    # Make sure the object stays within the boundaries of the screen
    object_x = max(0, min(object_x, screen_width - object_width))
    object_y = max(0, min(object_y, screen_height - object_height))
