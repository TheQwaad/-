from random import randint
from ChangeColor import *
from tkinter import *
import pygame
import sys
import os

with open('parametres/lens_type.txt') as file:
        lens_type = file.read()
lens_types = ['convex','concave','biconvex','biconcave']
lens_types_ru = ['Выпуклая','Вогнутая',
                 'Двояковыпуклая','Двояковогнутая']
colors = [(255,0,0),(0,255,0),(0,0,255),
          (255,255,0),(255,0,255),(0,0,0)]
key = ''    
pygame.display.set_icon(pygame.image.load("images/icon1.ico"))
pygame.display.set_caption('Линза')
pygame.init()
W = 800
H = 600
FPS = 60
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
Running = True
Dont_Touch = False
ChangeColor(0)

root = Tk()
root.resizable(width = False, height = False)
root.title('Конфигурация')

f1 = Frame()
f1.pack(side=LEFT, padx=40)
lbox = Listbox(f1,width = 15, height = 8)
lbox.pack(fill = Y)
name = Label(f1)
name.pack(fill=X)
bset = Button(f1, text="Выбрать тип")
bset.pack(fill=X)

f2 = Frame()
f2.pack(side = RIGHT,padx = 40)
var = IntVar()
var.set(0)
red = Radiobutton(f2,text="Красный", variable=var, value=0)
red.pack(fill=Y)
green = Radiobutton(f2,text="Зелёный", variable=var, value=1)
green.pack(fill=Y)
blue = Radiobutton(f2,text="Синий", variable=var, value=2)
blue.pack(fill=Y)
yellow = Radiobutton(f2,text="Жёлтый", variable=var, value=3)
yellow.pack(fill = Y)
purple = Radiobutton(f2,text="Фиолетовый", variable=var, value=4)
purple.pack(fill=Y)
purple = Radiobutton(f2,text="Чёрный", variable=var, value=5)
purple.pack(fill=Y)
bcolor = Button(f2, text = 'Выбрать цвет')
bcolor.pack(fill=Y)


for i in ('Двояковогнутая','Двояковыпуклая','Вогнутая','Выпуклая'):
    lbox.insert(0,i)

with open('parametres/lens_type.txt') as file:
    lens_type = file.read()
  
class Ray(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, mode,number):
        self.start_x = x
        self.start_y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.mode = mode
        self.number = number
    def to_start(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
    def change_direction(self):
        
        global lens_type
        if self.rect.x <= W//2+200:
            if lens_type == 'biconvex':
                if W//2-26 <= self.rect.x < W//2 + 32:
                    self.rect.y += 1 * self.mode * -1
                elif self.rect.x >= W//2 + 32:
                    self.rect.y += 2 * self.mode * -1
            elif lens_type == 'convex':
                if self.rect.x >= W//2-26:
                    self.rect.y += 1 * self.mode * -1
            elif lens_type == 'biconcave':
                if W//2-20 <= self.rect.x < W//2 + 30:
                    self.rect.y += 1 * self.mode
                elif self.rect.x >= W//2 + 30:
                    self.rect.y += 2 * self.mode
            elif lens_type == 'concave':
                if self.rect.x >= W//2-20:
                    self.rect.y += 1 * self.mode
    def draw(self):
        if self.rect.x < W//2+200:
            self.rect.x += 2
class Lens(pygame.sprite.Sprite):
    def __init__(self):
        global lens_type
        pygame.sprite.Sprite.__init__(self)
        print('images/' + lens_type+'.png')
        self.image = pygame.image.load('images/' + lens_type+'.png').convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(W//2,H//2))
    def draw(self):
        global lens_type
        self.image = pygame.image.load('images/' + lens_type+'.png').convert_alpha()
        self.rect = self.image.get_rect(center=(W//2,H//2))


def LensUpdate():
    sc.blit(Lens.image, Lens.rect)
    Lens.draw()
def RaysUpdate():
    sc.blit(Ray1.image, Ray1.rect)
    Ray1.draw()
    Ray1.change_direction()
    sc.blit(Ray2.image, Ray2.rect)
    Ray2.draw()
    Ray2.change_direction()
    sc.blit(Ray3.image, Ray3.rect)
    Ray3.draw()
    Ray3.change_direction()
def Reload():
    print('images/' + lens_type+'.png')
    global Ray1, Ray2, Ray3
    sc.fill(WHITE)
    Ray1.kill()
    Ray2.kill()
    Ray3.kill()
    LensUpdate()
    Ray1 = Ray(W//2-300,H//2 - 80, 'images/ray.png',-1,1)
    Ray2 = Ray(W//2-300,H//2, 'images/ray.png',0,2)
    Ray3 = Ray(W//2-300,H//2 + 80, 'images/ray.png',1,3)
def SetType():
    global key, lens_types, lens_type, Dont_Touch
    Dont_Touch = True
    lens_type = lens_types[key[0]]
    file = open('parametres/lens_type.txt','w')
    file.write(lens_types[key[0]])
    file.close()
    Reload()
    Reload()
    Dont_Touch = False
def ChangeColorButton():
    i = var.get()
    ChangeColor(i)
    Reload()
    Reload()
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

bset.configure(command = SetType)
bcolor.configure(command = ChangeColorButton)
    
sc.fill(WHITE)
Lens = Lens()
LensUpdate()
Ray1 = Ray(W//2-300,H//2 - 80, 'images/ray.png',-1,1)
Ray2 = Ray(W//2-300,H//2, 'images/ray.png',0,2)
Ray3 = Ray(W//2-300,H//2 + 80, 'images/ray.png',1,3)

while Running:
    if not Dont_Touch:
        with open('parametres/lens_type.txt') as file:
            s = file.read()
            if s != lens_type and lens_type != '':
                lens_type = s
                Reload()
                RaysUpdate()
                LensUpdate()
                RaysUpdate()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Running = False
            pygame.quit()
            root.destroy()

    RaysUpdate()
    
    pygame.display.update()
    pygame.time.delay(20)
    
    try:   
        root.update()
        key = list(lbox.curselection())
        if len(key) != 0:
            name.configure(text = lens_types_ru[key[0]])
    except Exception:
        Running = False
        pygame.quit()


