from object3D import *
import pygame as pg
from sys import exit

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))

    def create_objects(self):
        self.object = Object3D(self)
    
    def run(self):
        while True:
            self.draw()
            [exit() for e in pg.event.get() if e.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
