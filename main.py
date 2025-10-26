from run import Run
from playing import Playing
from renderer import Renderer
from storage import Storage, FoodsCounter, SlimesCounter
from pygame import quit as pygame_quit
storage = Storage()
food_counter = FoodsCounter(storage)
slime_counter = SlimesCounter(storage)
renderer = Renderer(storage.all_sprites)
play = Playing(storage, renderer, food_counter)
run = Run(play)
slime_counter.slime_add_logic(1, 50)
if __name__ == '__main__':
    run.run()
pygame_quit()