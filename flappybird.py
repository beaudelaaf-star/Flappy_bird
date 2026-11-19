import pygame
import random
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock() 
fps = 60
screenwidth = 864
screenheight = 936


screen = pygame.display.set_mode((screenwidth
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
lastpipe = pygame.time.get_ticks()


#loading images
bg = pygame.image.load("bg.png")
ground_img = pygame.image.load("floor.png")
restart_img = pygame.image.load("RESTART.png"


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
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]=
                action = True
        screen.blit(self.image,(self.rect.x,s
        return action


class Bird():
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for  i in range(1,3):
            img = pygame.image.load(f"bird{i}
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
                    self.rect.y = self.rect.y
        if gameover == False:
            #jump
            if pygame.mouse.get_pressed()[0] 
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] 
                self.clicked = False


            flap_cooldown = 5
            self.counter = self.counter +1 
            if self.counter > self.flap_coold
                self.counter = 0
                self.index = self.index +1
                if self.index >= len(self.ima
                    self.index = 0
                self.image = self.images[self
                # rotate the bird
            self.image = pygame.transform.rot
        else:
            self.image = pygame.transform.rot




class Pipe(pygame.sprite.Sprite):
    def __init__ (self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe.
        self.rect = self.image.get_rect()
         #position variable determines if the
        #position 1 is from the top, -1 is fr
        if pos  == 1:
            self.image = pygame.transform.fli
            self.rect.bottomleft = [x,y-int(p
        if pos  == -1:
            self.rect.topleft = [x,y+int(pipe


    def update(self):
        self.rect.x -=scroll_speed
        if self.rect.right <0:
            self.kill()                      






pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
flappy = Bird(100,int(screenheight/2))
bird_group.add(flappy)
button = Button(screenwidth//2-50,screenheigh
run = True


while True:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground_img,(ground_scroll,768
    if len(pipe_group)>0:
        if bird_group.sprites()[0].rect.left>
             and bird_group.sprites()[0].rect
             and passpipe == False:
            passpipe = True
            if passpipe == True:
                if bird_group.sprites()[0].re
                    score += 1
                    passpipe = False
    draw_text(str(score),font,white,int(scree




    #look for collision
    if pygame.sprite.groupcollide(bird_group,
        gameover = True 
    if flappy.rect.bottom >768:
        gameover = True
        flying = False




    if flying == True and gameover == False:
        timenow = pygame.time.get_ticks()
        if timenow - lastpipe > pipefrequency
            pipeheight = random.randint(-100,
            bottompipe = Pipe(screenwidth,int
            toppipe = Pipe(screenwidth,int(sc
            pipe_group.add(bottompipe)
            pipe_group.add(toppipe)
            lastpipe = timenow 
        pipe_group.update()
        ground_scroll = ground_scroll - scrol
        if abs(ground_scroll) > 35:
            ground_scroll = 0
    if gameover == True:
        if button.draw():
            gameover = False
            score = reset_game()
    for event in pygame.event.get:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDO
            flying = True
    pygame.display.update()
pygame.quit()






                                


    


         
                 











   
