import pygame

pygame.init()
window = pygame.display.set_mode(size=(600, 400))
while True:
    # Check all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # End pygame
