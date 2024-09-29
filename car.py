import pygame
import sys
import math
import os
import random
print(os.getcwd())


pygame.init()
# sounds on 
pygame.mixer.music.load("cyber.wav")
pygame.mixer.music.play()
wn = pygame.display.set_mode((360, 639)) 
pygame.display.set_caption("Car Racing")
logo = pygame.image.load("car.png")

# Set the window icon
pygame.display.set_icon(logo)
#result
score_value=0
font = pygame.font.SysFont('Arial', 30, bold=True)
score_x=140
score_y=100
#final result display
crash_x=125
crash_y = 250


game_exit = False
bg = pygame.image.load("back1.jpg")
#lambo image
car=pygame.image.load("red2.png")
img_x=150
img_y=550
img_xchange=0
img_ychange=500



#for opp side 
car1=pygame.image.load("white.png")
img1_x=30
img1_y=200
img1_xchange=0
img1_ychange=0.2
car2=pygame.image.load("black.png")
img2_x=200
img2_y=300
img2_xchange=0
img2_ychange=0.2

def car_image  (x,y):
    wn.blit(car,(x,y))
def car_1 (x,y):
    wn.blit(car1,(x,y))
def car_2 (x,y):
    wn.blit(car2,(x,y))
def crash(img_x, img_y, img1_x, img1_y):
    
    distance = math.sqrt(math.pow(img_x - img1_x, 2) + math.pow(img_y - img1_y, 2))

    if distance<50:
      return True
    else:
     return False
def crash(img_x, img_y, img2_x, img2_y):
    
    distance = math.sqrt(math.pow(img_x - img2_x, 2) + math.pow(img_y - img2_y, 2))

    if distance<50:
      return True
    else:
     return False
def show_score(x,y):
   font_score=font.render("Score:"+str(score_value),True,(0,255,255))  
     #we have use str cause only string and str can be add 
   wn.blit(font_score,(x,y))
def show_crash(x, y):
    font = pygame.font.SysFont(None, 27)  
    font_crash = font.render("CAR CRASHED!!!", True, (0, 255, 255))  #
    wn.blit(font_crash, (x, y))


while not game_exit:
   wn.blit(bg, (0, 0,))  # Draw the background image

   for event in pygame.event.get():

          if event.type == pygame.QUIT:

            game_exit = True

          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                img_xchange = 0.15 #speed of car
            if event.key == pygame.K_LEFT:
                img_xchange = -0.15
          
               
   img_x += img_xchange
   img1_y+=img1_ychange
   img2_y+=img2_ychange
    #boundry stop
   if img_x<1:
     img_x=1
   elif img_x>270:
       img_x=270
       
# for a car moving like a loop
   if img1_y>639:
       img1_y=-100
       img1_x=random.randint(65,270)
       score_value+=1
   if img2_y>630:
       img2_y=-101
       img2_x=random.randint(65,270)
       score_value+=1

   collision=crash(img_x, img_y, img1_x, img1_y)
   collisiontwo=crash(img_x, img_y, img2_x, img2_y)

       
        
       
    #call the uper fn
   car_image(img_x,img_y)    
   show_score(score_x,score_y)
   car_1 (img1_x,img1_y)    
   car_2 (img2_x,img2_y)    
   if collision:
     pygame.mixer.music.stop(
        
     )
     sound_crash=pygame.mixer.Sound("crash.wav")
     sound_crash.play()
     wn.fill((0,0,0))
     img1_ychange=0
     img2_ychange=0
     img_xchange = 0
     show_crash(crash_x,crash_y)
     show_score(score_x,score_y)
   elif collisiontwo:
     pygame.mixer.music.stop(
        
     )
     sound_crash=pygame.mixer.Sound("crash.wav")
     sound_crash.play()
     wn.fill((0,0,0))
     img1_ychange=0
     img2_ychange=0
     img_xchange = 0
     show_crash(crash_x,crash_y)
     show_score(score_x,score_y)
     


   pygame.display.update()  # Update the display

pygame.quit()
sys.exit()
