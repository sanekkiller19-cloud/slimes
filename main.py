import pygame
from game_controller import Run
from game_states import Playing, StoppedPlaying
from scene_manager import RendererPlaying, UpdaterPlaying
from sprites_counters import Storage, FoodsCounter, SlimesCounter
from random import randint
from settings import HEIGHT, WIDTH
pygame.init()


storage = Storage()
food_counter = FoodsCounter(storage)
slime_counter = SlimesCounter(storage)
updater = UpdaterPlaying(storage, food_counter, slime_counter)
renderer = RendererPlaying(storage.all_sprites)
play = Playing(storage, renderer, updater, food_counter)
stopped = StoppedPlaying()
run = Run(play,stopped)


slime_counter.slime_add_logic(1, randint(0, WIDTH), randint(0, HEIGHT))
if __name__ == '__main__':
    run.run()
pygame.quit()