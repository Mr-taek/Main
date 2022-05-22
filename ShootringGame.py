import random
from time import sleep
from turtle import window_height
import pygame
from pygame.locals import *
import os
from PIL import Image
import re
window_w=480
window_h=800

black=(0,0,0) # 
white=(255,255,255)

yellow=(255,255,50)
red=(255,50,50)
fps=60
Path=r"C:\Users\dlrms\OneDrive\Desktop\PyShooting"

class machine(pygame.sprite.Sprite):
    def __init__(self,path):
        name="fighter.png"
        path=os.path.join(path,name)
        super(machine,self).__init__() # 상위 전달자를..? 불러오기.call
        self.image=pygame.image.load(path)
        self.rect=self.image.get_rect()
        self.rect.x=int(window_w/2) # 중간에서 시작하기 위함
        self.rect.y=window_h-self.rect.height
        self.dx=0
        self.dy=0
    def update(self):
        self.rect.x+=self.dx
        self.rect.y+=self.dy
        # print(self.rect.x,self.rect.y)
        if self.rect.x-self.image.get_width()<0 or self.rect.x+self.image.get_width()>window_w:
            self.rect.x-=self.dx
        if self.rect.y-self.image.get_height()<0 or self.rect.y+self.image.get_height()>window_h:
            self.rect.y-=self.dy
        # if self.rect.x<0 or self.rect.x+10>window_w: #
        #     self.rect.x-=self.dx
        # if self.rect.y <0 or self.rect.y+self.rect.h> window_h: #640 인데 548...
        #     self.rect.y-=self.dy # 생각해보니 -가 맞나 ?
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def collide(self,sprites): # 객체에 충돌(COLIDE)
        for sprite in sprites:# sprite : in computer graphic where using 2D bitmap or combining animation. nowdys it means various image,text sorted in priority and combine.
            if pygame.sprite.collide_rect(self,sprite): # 오 .. self가 machine 자체고 sprite는 obj임. 이게 충돌하면
                return sprite
class attack(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed,path,level=1,type=0,pos=0):
        name="missile.png"
        image=os.path.join(path,name)
        sound=os.path.join(path,"missile.wav")
        super(attack,self).__init__()
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=xpos # machine의 self.rect.x
        self.rect.y=ypos # machine의 self.rect.y
        self.speed=speed
        # self.sound=pygame.mixer.Sound(sound)
        self.base_sound=pygame.mixer.Sound(os.path.join(Path,"missile.wav"))
        self.ultimate_sound=pygame.mixer.Sound(os.path.join(Path,"para.mp3"))
        self.level=level
        self.type=type
        self.count=0
        self.pos=pos
    # def launch(s 
    def launch(self):
        if self.level==1:
            self.base_sound.play()
        elif self.level==2:
            self.ultimate_sound.play()
    # def update(self): # 아...! updata 로 해서 이게 오류가 나네. 아래 저기에 pygame.sprite.Group() 이게 안에있는 class를 모으는데. 나중에 .update함. 근데 rock은 정확히 함수 이름이
    #     # update인데 얘는 아니라서 찾지를 못 한 것임. 
    #     # 바꾸니까 해결이 됨.
    #     self.rect.y-=self.speed
    #     print(self.rect.y,self.rect.h)
    #     if self.rect.y+self.rect.h <0:
    #         self.kill() # missile remove
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
    def collid(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite

class Rock(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed,path):
        name=[]
        for i in os.listdir(path):
            if re.search("^rock[\d]*",i):
                name.append(i)
        # print(name)
        name=tuple(name)
        super(Rock,self).__init__()
        self.image=pygame.image.load(os.path.join(path,random.choice(name)))#rock class가 호출될 때마다 무작위로 하나 생성
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.speed=speed
    def update(self):
        self.rect.y+=self.speed
    def out_of_screen(self):
        if self.rect.y>window_h:
            return True # 나간 수
def draw_text(text,font, surface, x, y, main_color):
    text_obj=font.render(text,True,main_color) # ..?
    text_rect=text_obj.get_rect()
    text_rect.centerx=x
    text_rect.centery=y
    surface.blit(text_obj,text_rect)

def occur_explosion(surface,x,y,path):
    name="explosion.png"
    ex_img=os.path.join(path,name)
    explosion_image=pygame.image.load(ex_img)
    explosion_rect=explosion_image.get_rect()
    explosion_rect.x=x
    explosion_rect.y=y
    surface.blit(explosion_image,explosion_rect) # 그리기 ..? 이미지를 사각형에 대해서 화면에 그리기.
    name=[]
    for i in os.listdir(path):
        if re.search(r"^explosion[\d*]",i):
            name.append(i)
    explosion_sounds=tuple(name)# 폭발 발생후 소리.
    explosion_sound=pygame.mixer.Sound(os.path.join(path,random.choice(explosion_sounds)))
    explosion_sound.play()

def game_loop(path):
    name=os.path.join(path,"NanumGothic.ttf")
    back=os.path.join(path,"background.png")
    default_font=pygame.font.Font(name,30)
    background=pygame.image.load(back)
    gameover_sound=pygame.mixer.Sound(os.path.join(path,"gameover.wav"))
    pygame.mixer.music.load(os.path.join(path,"music.wav"))
    pygame.mixer.music.play(-1) # loop parameter -1, means infinite
    fps_clock=pygame.time.Clock()
    fighter = machine(path)
    missiles=pygame.sprite.Group() # 여러개가 들어갈 수 있어야 해서. 아~ 한 화면에. 
    rocks=pygame.sprite.Group() # 여러가지 객체들어가야해서. 여러 객체가 겹쳐도 알아서 조절해줌.
    occur_prob=40 # 생성확률. 아마 rocks인듯.
    shot_count=0 # 맞힌 운석개수
    count_missed=0 #놓힌 운석개수
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN: # keydown 의 의미는 화살표 키가 눌림을 의미.
                if event.key==pygame.K_LEFT:
                    fighter.dx-=1
                elif event.key == pygame.K_RIGHT:
                    fighter.dx+=1
                elif event.key==pygame.K_UP:
                    fighter.dy-=1
                elif event.key==pygame.K_DOWN:
                    fighter.dy+=1
                if event.key==pygame.K_SPACE: 
                    missile=attack(fighter.rect.x,fighter.rect.y,10,path=Path) #d여기 다르게함.
                    missile.launch()
                    missiles.add(missile)
                if event.key==pygame.K_k: 
                    li=[]
                    for i in range(20):
                        if i%2==0:
                            li.append(attack(fighter.rect.x,fighter.rect.y,10,Path,2,0,pos=i))
                        else:
                            li.append(attack(fighter.rect.x+30,fighter.rect.y,10,Path,2,1,pos=i))# 무기 발사 위치로 +30
                    
                        li[0].launch()
                    missiles.add(li)
            # if event.type==pygame.KEYUP:
                # fighter.dx=0 # 이렇게 하면 매끄럽지가 않음.
                # fighter.dy=0 # 이렇게 하면 매끄럽지가 않음.

            # else: key up 부분은 굳이 필요가 없을 듯.
        screen.blit(background,background.get_rect()) # 배경화면애 새 화면으로 계속 업그레이드 시켜주는 것. 없으면 모든 객체가 화면에 사라지지 않고 남음.
        occur_of_rocks=1+int(shot_count/300) 
        min_rick_spped=1+int(shot_count/200) # 200개 맞추는 순간 1+2 = 3 레벨
        max_rick_spped=1+int(shot_count/100) # 100개 맞추는 순간 1+1=2
        if random.randint(1,occur_prob) ==1:
            for i in range(occur_of_rocks):
                speed=random.randint(min_rick_spped,max_rick_spped)
                rock=Rock(random.randint(0,window_w-30),0,speed,path=path)# y=0 은 맨 위
                rocks.add(rock) # 없으면 화면에 ROCK이 아 무것도 안나옴.
        draw_text("파괴 운석 : {}".format(shot_count), default_font, screen,100,20,yellow)
        draw_text("그냥 운석 : {}".format(shot_count), default_font, screen,400,20,red)
        for missile in missiles:
            rock=missile.collid(rocks)
            if rock:
                missile.kill()
                rock.kill()
                occur_explosion(screen,rock.rect.x,rock.rect.y,path)
                shot_count+=1

        for rock in rocks:
            if rock.out_of_screen():
                rock.kill()
                count_missed+=1
        rocks.update() # 없으면 ROCK이 생성은 되는데 떨어지질 않음.
        rocks.draw(screen) # 없으면 ROCK이 생성은 되는데 보이질 않음.
        missiles.update()
        missiles.draw(screen)
        fighter.update()
        fighter.draw(screen)
        pygame.display.flip()

        if fighter.collide(rocks) or count_missed >=3:
            pygame.mixer.stop()
            occur_explosion(screen,fighter.rect.x,fighter.rect.y,path)
            pygame.display.update()
            gameover_sound.play()
            sleep(1)
            done=True
        fps_clock.tick(fps)
    return "game_menu"

def game_menu(path):
    image=os.path.join(path,"background.png")
    start_image=pygame.image.load(image)
    screen.blit(start_image,[0,0])
    draw_x=int(window_w/2)
    draw_y=int(window_h/4)
    font_70=pygame.font.Font(os.path.join(path,"NanumGothic.ttf"),70)
    font_40=pygame.font.Font(os.path.join(path,"NanumGothic.ttf"),40)
    draw_text("protect earth",font_70,screen,draw_x,draw_y,yellow)
    draw_text("press enter",font_40,screen,draw_x,draw_y+200,white)
    draw_text("game start",font_40,screen,draw_x,draw_y+250,white)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_RETURN:
                return 'play'
        if event.type==QUIT:
            return "quit"
    return "game_menu"

def main():
    global screen
    pygame.init()
    screen=pygame.display.set_mode((window_w,window_h))
    pygame.display.set_caption("Pyshooting")
    action="game_menu"
    while action !='quit':
        # print("main")
        if action=="game_menu":
            action=game_menu(Path)
        elif action =="play":
            action=game_loop(Path)
    pygame.quit()

if __name__=="__main__":
    main()
        #rock_images=
# k=os.path.join(path,"fighter.png")

# with Image.open(k) as im:
#     im.show("title")


# for i in os.listdir(path):
#     if re.search(r"^rock",i):
#         name.append(i)
