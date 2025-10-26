from settings import BLACK, clock, screen
import pygame
class Renderer:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
    def render(self):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)