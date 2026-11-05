import pygame
import random
from pygame.locals import *


pygame.init()
clock = pygame.time.clock()
fps = 60
screenwidth = 864
screenheight = 936


screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Flappy Bird")


font = pygame.font.SysFont("Buahaus 93",60)
white = (255,255,255)


ground_scroll = 0
scroll_speed = 5
flying = False
gameover = False
pipegap = 150
pipefrequency = 1500
score = 0
passpipe = False 


#loading images
bg = pygame.image.load("bg.png")
ground_img = pygame.load("floor.png")
restart_img = pygame.load("RESTART.png")


def draw_text(text, font, text_col,x, y):
    img = font.render(text,True, text_col)
    screen.blit(img,(x,y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screenheight/2)
    score = 0
    return score


class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.getrect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action = True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action


class Bird():
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self.images)
        self.images = []
        self.index = 0
        self.counter = 0
        for  i in range(1,3):
            img = pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False
    def update(self):
        if flying == True:
            #applying gravity
            self.vel = self.vel + 0.5
            if self.vel > 8:
                self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y = self.rect.y + int (self.vel)
        if gameover == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False


                flap_cooldown = 5
                self.counter = self.counter +1 
                if self.counter < self.flap_cooldown:
                    self.counter = 0
                    self.index = self.index +1
                    if self.index >= len(self.images):
                        self.index = 0
                    self.image = self.images[self.index]
                # rotate the bird
                self.image = pygame.transform.rotate(self.images[self.index
            else:
                self.image = pygame.transform.rotate(self.images[self.index




class Pipe(pygame.sprite.Sprite):
    def __init__ (self.x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pipe.png)                         
                        






pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
flappy = Bird(100,int(screenheight/2))
bird_group.add(flappy)
button = Button(screenwidth//2-50,screenheight//2-100,restart_img)
run = True



























