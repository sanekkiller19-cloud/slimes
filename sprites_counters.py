import random as rd
from sprites import Food, pygame, WIDTH, HEIGHT, Slime


class Storage:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()
        self.slimes = pygame.sprite.Group()
    def add_food(self, sprite):
        self.all_sprites.add(sprite)
        self.foods.add(sprite)
    def add_slime(self, sprite):
        self.all_sprites.add(sprite)
        self.slimes.add(sprite)


class SlimesCounter:

    def __init__(self, storage):
        self.storage = storage

    def slime_add_logic(self, count, x, y, sat=50):
        for _ in range(count):
            slime = Slime(x, y, sat)
            self.storage.add_slime(slime)


class FoodsCounter:
    FOOD_TIME = 1000
    def __init__(self, storage):
        self.storage = storage
        self.food_timer = pygame.time.get_ticks()

    def food_add_logic(self):
        current = pygame.time.get_ticks()
        if current - self.food_timer > self.FOOD_TIME:
            new_food = Food(rd.randint(0, WIDTH), rd.randint(0, HEIGHT))
            self.storage.add_food(new_food)
            self.food_timer = current
