from asyncio.windows_events import NULL
from re import S
import pygame
import os
from pygame.locals import *
import numpy as np
import random
Path=r"C:\Users\dlrms\OneDrive\Desktop\PyShooting"
window_h=pygame.image.load(os.path.join(Path,"background.png")).get_height()
window_w=pygame.image.load(os.path.join(Path,"background.png")).get_width()
screen=pygame.display.set_mode((window_w,window_h))
pygame.init() # sound 를 사용하려면 이게 필수이네.
class character(pygame.sprite.Sprite):
    def __init__(self):
        super(character,self).__init__()
        self.charact=pygame.image.load(os.path.join(Path,"fighter.png"))
        self.rect=self.charact.get_rect()
        self.rect.x=int(window_w/2)
        print(self.rect.height)
        self.rect.y=window_h-self.rect.height# 화면 세로의 전체 크기에 들어오려면 이미지의 사이즈를 빼줘야 등장함
        self.dx=0
        self.dy=0
    def update(self):
        self.rect.x+=self.dx
        self.rect.y+=self.dy
        if self.rect.x<0 or self.rect.x>window_w:
            self.rect.x-=self.dx
        if self.rect.y-self.charact.get_height()<0 or self.rect.y+self.charact.get_height()>window_h:
            self.rect.y-=self.dy
    def draw(self):
        screen.blit(self.charact,self.rect)
class attack(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,level=1,type=0,pos=0):
        self.image=pygame.image.load(os.path.join(Path,"missile.png"))
        self.base_sound=pygame.mixer.Sound(os.path.join(Path,"missile.wav"))
        self.ultimate_sound=pygame.mixer.Sound(os.path.join(Path,"para.mp3"))
        super(attack,self).__init__()
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.speed=10
        self.level=level
        self.type=type
        self.count=0
        self.pos=pos
    def launch(self):
        if self.level==1:
            self.base_sound.play()
        elif self.level==2:
            self.ultimate_sound.play()
    def update(self):
        if self.level==1:
            self.rect.y-=self.speed
            if self.rect.y+self.rect.h<0:
                self.kill()
        elif self.level==2:
            self.count+=1
            if self.type==0: # 왼쪽 레이저포
                self.rect.y-=1
                self.rect.x-=self.pos
                if self.count>15:
                    self.rect.y-=5
                    self.rect.x+=(self.pos)
            else:# 오른쪽 레이저포
                self.rect.y-=1
                self.rect.x+=self.pos
                if self.count>15:
                    self.rect.y-=5
                    self.rect.x-=(self.pos)
            if self.rect.y+self.rect.h<0:
                self.count=0
                self.kill()
    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite


class game:
    def __init__(self,path):
        self.path=path
        self.background=pygame.image.load(os.path.join(path,"background.png"))
    def game_menu(self):
        start_image=self.background
        screen.blit(start_image,[0,0])
        pygame.display.update() # 이것만 있어서는 안되누.
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN: # enter를 의미함.
                    return 'play'
            if event.type==QUIT:
                return "quit"
        return "game menu"  # 이게 핵심! start 에선 while 돌아가는데.. recursive로 돌리는 것임.
        # self.game_menu(path) 도 가능하지만 game menu도 가능!
    def play(self):
        cha=character()
        fps_clock=pygame.time.Clock()
        Attacks=pygame.sprite.Group()
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
                    import sys
                    sys.exit()
                pressed=pygame.key.get_pressed()
                # print(pressed)
                if pressed[pygame.K_UP]: cha.dy-=2
                if pressed[pygame.K_DOWN]: cha.dy+=2
                if pressed[pygame.K_LEFT]: cha.dx-=2
                if pressed[pygame.K_RIGHT]: cha.dx+=2
                if pressed[pygame.K_SPACE]: 
                    at=attack(cha.rect.x,cha.rect.y,level=1)
                    at.launch()
                    Attacks.add(at)
                if pressed[pygame.K_k]:
                    li=[]
                    for i in range(20):
                        if i%2==0:
                            li.append(attack(cha.rect.x,cha.rect.y,2,0,pos=i))
                        else:
                            li.append(attack(cha.rect.x+30,cha.rect.y,2,1,pos=i))# 무기 발사 위치로 +30
                    
                        li[0].launch()
                    Attacks.add(li)
                    # Attacks.add(at2)
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        cha.dx=0
                    else:
                        cha.dy=0
            screen.blit(self.background,self.background.get_rect())
            cha.update()
            cha.draw()
            Attacks.update()
            Attacks.draw(screen)
            fps_clock.tick(60)
            pygame.display.flip() # 게임 화면에서 무언가 출력되기 위한 핵심! 이게 없으면 뭐가 뜨지도 않음
    def start(self):
        # global screen # global 변수는 가급적 사용하지 않는다 원칙으로 안 쓴다.
        pygame.display.set_caption("shootung star")
        action="game menu"
        while action!="quit":
            if action=="game menu":
                action=self.game_menu()
            elif action=="play":
                action=self.play()
        pygame.quit()

Path=r"C:\Users\dlrms\OneDrive\Desktop\PyShooting"
st=game(Path)
st.start()

# 운석 깬 횟수대로. 5의 배수 10의 배수. 5개 깨면 레벨업. 1.5

class Rock(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed,path):
        super(Rock,self).__init__()
        self.image=pygame.image.load(os.path.join(path,"rock01.png"))
        # self.sound=pygame.mixer.Sound(os.path.join(path,"rocksound.wav"))
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.speed=speed
    def update(self):
        self.rect.y+=self.speed
    def out_of_screen(self):
        if self.rect.y>window_h:
            return True