from tkinter.tix import WINDOW
import pygame
from settings import *
from random import choice, randint

class BG(pygame.sprite.Sprite): 
    def __init__(self,groups):
        super().__init__(groups) #lokacja grupy
        bg__image = pygame.image.load('bg_5.png').convert()
        full_sized_image = pygame.transform.scale(bg__image,(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.image=pygame.Surface((WINDOW_WIDTH*2,WINDOW_HEIGHT))
        self.image.blit(full_sized_image, (0,0))
        self.image.blit(full_sized_image, (WINDOW_WIDTH,0))
        self.rect = self.image.get_rect(topleft=(0,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 300*dt
        self.rect.x=round(self.pos.x)
        if self.rect.centerx <= 0:
            self.pos.x=0
        self.rect.x=round(self.pos.x)

class Ground(pygame.sprite.Sprite):
    def __init__(self,groups,scale_factor):
        super().__init__(groups)
        self.sprite_type='ground'

        #image
        ground_surf=pygame.image.load('ground.png').convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size())*scale_factor)

        #position
        self.rect = self.image.get_rect(bottomleft=(0,WINDOW_HEIGHT))
        self.pos=pygame.math.Vector2(self.rect.topleft)

        #mask
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self,dt):
        self.pos.x -= 360*dt
        if self.rect.centerx <=0:
            self.pos.x=0
        
        self.rect.x=round(self.pos.x)

class Plane(pygame.sprite.Sprite):

    def __init__(self, groups, scale_factor):
        super().__init__(groups)

        #image
        self.import_frames(scale_factor)
        self.frame_index=0
        self.image=self.frames[self.frame_index]

        #rect
        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH/20, WINDOW_HEIGHT/2))
        self.pos=pygame.math.Vector2(self.rect.topleft)

        #movement
        self.gravity=700
        self.direction=0

        #mask
        self.mask = pygame.mask.from_surface(self.image)

        #sound
        self.jump_sound=pygame.mixer.Sound('jump.mp3')
        self.jump_sound.set_volume(0.3)


    def import_frames(self, scale_factor):
        self.frames=[]
        for i in range(3):
            surf=pygame.image.load(f'alien{i}.png').convert_alpha()
            scaled_surface=pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size())*scale_factor)
            self.frames.append(scaled_surface)
    
    def apply_gravity(self,dt):
        self.direction += self.gravity*dt
        self.pos.y += self.direction*dt
        self.rect.y=round(self.pos.y)

    def jump(self):
        self.jump_sound.play()
        self.direction= -450
    
    def animate(self,dt):
        self.frame_index+=10*dt
        if self.frame_index >= len(self.frames):
            self.frame_index=0
        self.image=self.frames[int(self.frame_index)]

    def rotate(self):
        rotated_plane=pygame.transform.rotozoom(self.image,-self.direction*0.06,1)
        self.image=rotated_plane
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,dt):
        self.apply_gravity(dt)
        self.animate(dt)
        self.rotate()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        self.sprite_type='obstacle'
        
        orientation=choice(('up','down'))
        surf=pygame.image.load(f'{choice((0,1))}.png').convert_alpha()
        self.image=pygame.transform.scale(surf,pygame.math.Vector2(surf.get_size())*scale_factor)

        x=WINDOW_WIDTH+randint(40,100)

        if orientation=='up':
            y=WINDOW_HEIGHT-randint(110,160)
            self.rect=self.image.get_rect(midbottom=(x,y))
        else: 
            y=randint(-50,-10)
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect=self.image.get_rect(midtop=(x,y))

        self.pos=pygame.math.Vector2(self.rect.topleft)

        #mask
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self,dt):
        self.pos.x-=400*dt
        self.rect.x=round(self.pos.x)
        if self.rect.right<=-100:
            self.kill()
