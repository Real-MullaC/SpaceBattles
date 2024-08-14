import pygame
import random
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Item(object):
    def __init__(self, x: int, y: int, width: int, height: int, velocity: int, image, screen_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.image = image
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen_size = screen_size
        self.active = True

    def draw(self, surface):
        if self.active:
            surface.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.velocity
        self.hitbox.y = self.y
        if self.y > self.screen_size[1]:
            self.active = False

class Heart(Item):
    def __init__(self, x: int, y: int, image, screen_size):
        super().__init__(x, y, 32, 32, 2, image, screen_size)

    def update(self):
        try:
            self.move()
        except Exception as e:
            print(f"Error updating Heart: {e}")

class Crystal(Item):
    def __init__(self, x: int, y: int, image, screen_size):
        super().__init__(x, y, 32, 32, 2, image, screen_size)

    def update(self):
        try:
            self.move()
        except Exception as e:
            print(f"Error updating Crystal: {e}")