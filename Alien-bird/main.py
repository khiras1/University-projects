import pygame, sys, time
from settings import *
from sprites import BG, Ground, Plane, Obstacle

class Game:
    def __init__(self): 
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #stworzenie interfejsu, rozmiar
        pygame.display.set_caption('My Flappy Bird, I think') #tytul gry
        self.clock=pygame.time.Clock() #zegarek
        self.active=True #ustawienie ze gra jest aktywa

        self.all_sprites=pygame.sprite.Group() #wszystkie obiekty w grze
        self.collision_sprities=pygame.sprite.Group()

        #scaling
        bg_height = pygame.image.load('bg_5.png').get_height()
        self.scale_factor=WINDOW_HEIGHT/bg_height

        #sprite setup
        BG(self.all_sprites)
        Ground([self.all_sprites, self.collision_sprities], self.scale_factor)
        self.plane=Plane(self.all_sprites, self.scale_factor/20)

        #timer
        self.obstacle_timer=pygame.USEREVENT +1
        pygame.time.set_timer(self.obstacle_timer,1400)

        #text
        self.font=pygame.font.Font('BD_Cartoon_Shout.ttf',30)
        self.score=0
        self.start_offset=0

        #menu
        self.menu_surf=pygame.image.load('menu.png').convert_alpha()
        self.menu_rect= self.menu_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.high_score=0

        #music
        self.music=pygame.mixer.Sound('music.mp3')
        self.music.set_volume(0.6)
        self.music.play(loops=-1) #nieskonczony loop

    def draw_text(self, surf, text, size, x, y):
        self.font=pygame.font.Font('BD_Cartoon_Shout.ttf', size)
        self.text_surface=self.font.render(text, True, 'white')
        self.text_rect=self.text_surface.get_rect(midtop=(x,y))
        surf.blit(self.text_surface, self.text_rect)

        

    def show_go_window(self):
        window=self.display_surface
        window.fill('purple')
        self.draw_text(window, "Najlepszy wynik", 30, WINDOW_HEIGHT/2, WINDOW_WIDTH/2)

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprities, False, pygame.sprite.collide_mask) or self.plane.rect.top <= 0:
            for sprite in self.collision_sprities.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.active=False
            self.plane.kill() 
    
    def display_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset)//1000
            y= WINDOW_HEIGHT/10
        else:
            y=WINDOW_HEIGHT/2 + (self.menu_rect.height/1.5)

        score_surf = self.font.render(str(self.score),True,'white')
        score_rect=score_surf.get_rect(midtop=(WINDOW_WIDTH/2,y))
        self.display_surface.blit(score_surf, score_rect)
    
    def run(self):
        last_time=time.time()

        while True:
            #delta time
            dt=time.time() - last_time #delta time, klatki na sekunde
            last_time=time.time()
            
            #event
            for event in pygame.event.get(): #event loop
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane = Plane(self.all_sprites, self.scale_factor/20)
                        self.active=True
                        self.start_offset=pygame.time.get_ticks()

                if event.type==self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprities], self.scale_factor*0.35)
            
            #game logic
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.active:
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf, self.menu_rect)

            pygame.display.update() #updatujemy caly czas gre
            self.clock.tick(FRAMERATE) #




if __name__=='__main__': #czy nasz aktualny plik to main plik, jesli tak to odpalamy grę (klasą)
    game = Game()
    game.run()