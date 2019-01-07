import pygame
import random
from time import sleep

#게임에 사용되는 전역변수 정의

WHITE=(255,255,255)
RED=(255,0,0)

pad_width=480
pad_height=640

cat_width=62
cat_height=79

life_width=62
life_height=60

enemy_width=33
enemy_height=35

heart_width=28
heart_height=23

#게임에 등장하는 객체 드로잉

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

# 점수 계산  

def drawScore(count):

    global gamepad

    font = pygame.font.SysFont(None, 20)

    text = font.render('Score:' + str(count*30), True, WHITE)

    gamepad.blit(text,(0,0))

def drawPass(passed):

    global gamepad

    font = pygame.font.SysFont(None, 20)

    text = font.render('Passed:' + str(passed), True, RED)

    gamepad.blit(text,(70,0))



def dispMessage(text):

    global gamepad

    textfont = pygame.font.Font('freesansbold.ttf', 80)

    text = textfont.render(text, True, RED)

    textpos = text.get_rect()

    textpos.center = (pad_width/2, pad_height/2)

    gamepad.blit(text,textpos)

    pygame.display.update()

    sleep(2)

    #game_intro()

def gameover():

    global gamepad

    dispMessage('Game Over')
    game_intro()

def game_intro():
    global pamepad , title

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)  #이거넣으면 마우스 위치랑 이것저것 다 보여줌
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    runGame()      
        gamepad.fill(WHITE)
        drawObject(title,0,0)

        pygame.display.update()
        clock.tick(15)
                   
#게임 실행
def runGame():
    global gamepad, cat, clock, background
    global enemy, life , heart, shock

    check=False #충돌했을때 True로 설정되는 플래그
    checkL=False
    lifecount=5
    drawshock=0
    passed=0
    score=0
    j=0
    
    x=pad_width /2  # 중앙에서 시작하게 함
    y=pad_height /2

    x_change=0  #방향키를 조작할때 움직이게 하는 정도를 정의
    y_change=0

    enemy_x=random.randrange(0,pad_width-enemy_width) #적 가로픽셀 측정해서 범위지정
    enemy_y=0
    
    life_x=random.randrange(0,pad_width-life_width)
    life_y=0
    
    
    crashed=False

    while not crashed:
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                crashed=True

            #키누를때 동작 설정 -누르면 움직이고 떼면 멈춤-
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_UP:
                    y_change-=5
                elif event.key==pygame.K_DOWN:
                    y_change+=5
                elif event.key==pygame.K_RIGHT:
                    x_change+=7
                elif event.key==pygame.K_LEFT:
                    x_change-=7
                
            if event.type==pygame.KEYUP:
                
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0

        y+=y_change
        x+=x_change
        
        gamepad.fill(WHITE)
        drawObject(background,0,0)
        
        
        #고양이가 화면 밖으로 벗어나지 않도록 설정
        if x < 0: 
            x = 0

        elif x > pad_width - cat_width:
            x = pad_width - cat_width
        if y < 0: 
            y = 0

        elif y > pad_height - cat_height:
            y = pad_height - cat_height

        drawObject(cat,x,y)
            
        #고양이와 적이 충돌했는지 체크
        

        if y<enemy_y+enemy_height:
            if(enemy_x > x and enemy_x < x + cat_width) or ( enemy_x + enemy_width > x and enemy_x + enemy_width < x + cat_width):
                check=True
        #적위치 조정
        enemy_y +=5

        if enemy_y >= pad_height:
            enemy_x=random.randrange(0,pad_width) #적 가로픽셀 지정해서 범위지정
            enemy_y=0
        
        if not check:
            drawObject(enemy,enemy_x,enemy_y)
        else:
            drawObject(shock,enemy_x,enemy_y)
            enemy_x=random.randrange(0,pad_width-enemy_width)
            enemy_y=0
            lifecount-=1
            check=False      

        #고양이와 우유가 충돌했는지 체크
        if y<life_y+life_height:
            if(life_x > x and life_x < x + cat_width) or ( life_x + life_width > x and life_x + life_width < x + cat_width):
                checkL=True

           
        #우유위치 조정
        life_y += 7 #우유가 enemy보다 빨리 떨어짐
            

        if life_y >= pad_height:
            life_x=random.randrange(0,pad_width)
            life_y=0
            passed+=1

        if not checkL:
            drawObject(life,life_x,life_y)
        else:
            drawObject(shock,life_x,life_y)
            life_x=random.randrange(0,pad_width-life_width)
            life_y=0
            score+=1
            checkL=False


        if passed==5:
            gameover()


        if lifecount == 0:
            gameover()

        
       
        for i in range(1,lifecount+1):
            drawObject(heart,pad_width-i*(heart_width+5),0)
        drawScore(score)
        drawPass(passed)
        
           


        pygame.display.update()  #계속해서 화면에 표시
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, cat, clock, background , title
    global enemy,life, heart, shock

    
    pygame.init()
    gamepad=pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('Cat_watchOUT')
    
    cat=pygame.image.load('C:\\test\\cat.png')
    background=pygame.image.load('C:\\test\\background.png')
    
    title=pygame.image.load('C:\\test\\title.png')
    enemy=pygame.image.load('C:\\test\\lemon.png')
    life=pygame.image.load('C:\\test\\milk.png')
    heart=pygame.image.load('C:\\test\\life.png')
    shock=pygame.image.load('C:\\test\\shock.png')
    
    
    
    clock=pygame.time.Clock()
    game_intro()


initGame()
