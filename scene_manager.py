from settings import BLACK, clock, screen
import pygame
# RENDER


class RendererPlaying:

    def __init__(self, all_sprites):
        self.all_sprites = all_sprites

    def render(self):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)


# UPDATE


class UpdaterPlaying:

    def __init__(self, storage, food_counter, slimes_counter):
        self.storage = storage
        self.food_counter = food_counter
        self.slimes_counter = slimes_counter

    def all_sprites_update(self):
        self.storage.slimes.update(self.slimes_counter, self.storage.foods)
