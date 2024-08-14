import pygame
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Class for Projectile object

class Projectile(object):
    def __init__(self, x: int, y: int, width: int, height: int, velocity: int, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.image = pygame.transform.scale(image, (width, height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, downward=False):
        if downward:
            self.y += self.velocity
        else:
            self.y -= self.velocity
        self.hitbox.y = self.y