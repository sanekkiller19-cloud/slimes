from settings import pygame, COLORS, WIDTH, HEIGHT
import random as rd
class Slime(pygame.sprite.Sprite):
    SIZE = (48, 48)
    RADIUS = 24

    def __init__(self, x, y, satiety = 50):
        super().__init__()
        self.image = pygame.Surface(Slime.SIZE, pygame.SRCALPHA)
        self.color = rd.choice(COLORS)
        self.direction_time = pygame.time.get_ticks()
        pygame.draw.circle(self.image, self.color, (Slime.SIZE[0] // 2, Slime.SIZE[1] // 2), Slime.RADIUS)
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.vel = pygame.math.Vector2(0, 0)
        self.satiety = satiety

    def update(self, slimes_counter, foods):
        self.satiety -= 0.05
        self.time_logic()
        self.satiety_logic(slimes_counter)
        self.collide_food(foods)

        self.move_logic()

    def time_logic(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.direction_time > 1000:
            self.direction_time = pygame.time.get_ticks()
            self.vel = pygame.Vector2(rd.choice([3, -3, 0]), rd.choice([3, -3, 0]))

    def satiety_logic(self, slimes_counter):
        if self.satiety >= 100:
            self.satiety -= 50
            slimes_counter.slime_add_logic(1, self.pos.x , self.pos.y)
        if self.satiety <= 0:
            self.kill()

    def move_logic(self):
        self.pos += self.vel
        if self.pos.y < 0:
            self.pos.y = 0

        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH

        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.center = self.pos

    def collide_food(self, foods):
        for food in foods:
            if pygame.sprite.collide_rect(self, food):
                self.satiety += food.saturation
                food.kill()


class Food(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.size = rd.randint(1, 30)
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.color = rd.choice(COLORS)
        self.radius = self.size // 2
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), self.radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.calculate_saturation()

    def calculate_saturation(self):
        self.saturation = 0.7 * (self.rect.width + self.rect.height)
