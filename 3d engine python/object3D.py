import pygame as pg
from matrixFunctions import *
#import numpy


class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertexes = [
            (0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
            (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)
            ]

        self.faces = [
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)
            ]

    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix()
    
    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, pos):
        self.vertexes = self.vertexes @ scale(pos)

    def rotate_x(self, pos):
        self.vertexes = self.vertexes @ rotate_x(pos)

    def rotate_y(self, pos):
        self.vertexes = self.vertexes @ rotate_y(pos)

    def rotate_z(self, pos):
        self.vertexes = self.vertexes @ rotate_z(pos)
        

'''
class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([
            (0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
            (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)
            ])

        self.faces = np.array([
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)
            ])

    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, pos):
        self.vertexes = self.vertexes @ scale(pos)

    def rotate_x(self, pos):
        self.vertexes = self.vertexes @ rotate_x(pos)

    def rotate_y(self, pos):
        self.vertexes = self.vertexes @ rotate_y(pos)

    def rotate_z(self, pos):
        self.vertexes = self.vertexes @ rotate_z(pos)
'''
