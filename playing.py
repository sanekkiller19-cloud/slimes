import pygame
class Playing:
    def __init__(self, storage, renderer, food_counter):
        self.storage = storage
        self.renderer = renderer
        self.food_counter = food_counter
    def event_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
    def play(self):
        event = self.event_logic()
        if event is not None:
            return event
        self.update()
        self.food_counter.add_food()
        self.renderer.render()
    def update(self):
        self.storage.foods.update()
        self.storage.slimes.update(self.storage, self.storage.foods)
