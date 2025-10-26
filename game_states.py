import pygame



# STATES


class Playing:

    def __init__(self, storage, renderer, updater, foods_counter):
        self.storage = storage
        self.renderer = renderer
        self.updater = updater
        self.foods_counter = foods_counter

    def event_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "STOPPED"

    def play(self):
        event = self.event_logic()
        if event is not None:
            return event
        self.foods_counter.food_add_logic()
        self.updater.all_sprites_update()
        self.renderer.render()

class StoppedPlaying:

    def event_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "PLAYING"

    def stop(self):
        event = self.event_logic()
        if event is not None:
            return event
