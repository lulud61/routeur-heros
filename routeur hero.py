import pygame
from pygame.locals import QUIT
from random import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('routeur heros')



# Fond
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((173, 216, 230))


# Texte
font = pygame.font.Font(None, 36)
text = font.render("routeur heros", 1, (0, 0, 0))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)
font2 = pygame.font.Font(None, 50)
text2 = font2.render("perdu le noyaux est detruit", 1, (250 ,0, 0))


# Chargement de l'image
image = pygame.image.load("flare.png").convert()
imageconvoyeur = pygame.image.load("conveyor-0-0.png").convert()
imagerouteur = pygame.image.load("router.png").convert()
imageduo = pygame.image.load("duo.png").convert()
imagecoper = pygame.image.load("item-copper.png").convert()
imageboom = pygame.image.load("boom.png").convert()
imagefume = pygame.image.load("fume.png").convert()

resized_coper = pygame.transform.scale(imagecoper, (20, 20))
resized_duo = pygame.transform.scale(imageduo, (32, 32))
rotated_flare = pygame.transform.rotate(image, 180)
resized_fume=pygame.transform.scale(imagefume, (30,30))
resized_boom=pygame.transform.scale(imageboom, (40,40))





# Affichage initial
screen.blit(background, (0, 0))
pygame.display.flip()




noyaux=True
g=False
d=False
dg=False
dm=False
dd=False
condif1=False
condif2=False
condif3=False

score=0

acuvitesse=0
vitesseflare=0.25+acuvitesse
vitessetapis=0.5+acuvitesse

y2=700
x2=275

x4=250
y4=505


x5=300
y5=505

#genere les flare
nb=0
limit=2

#position des flare
yf1=-50
yf2=-50
yf3=-50

# Boucle principale
clock = pygame.time.Clock()
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    

    x3,y3=mouse_pos = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    
    #pour score
    font3 = pygame.font.Font(None, 30)
    text3 = font3.render(f"score: {score} ", 1, (0 ,0, 0))
    screen.blit(text3, (10,10))


    #pour aficher routeur et convoyeur
    
    screen.blit(resized_duo, (266 , 470))
    screen.blit(imagerouteur, (268 , 500))
    screen.blit(imageconvoyeur, (300 , 500))
    screen.blit(imageconvoyeur, (332 , 500))
    screen.blit(imageconvoyeur, (364 , 500))
    screen.blit(imageconvoyeur, (396 , 500))
    screen.blit(imageconvoyeur, (428 , 500))
    screen.blit(resized_duo, (485 , 500))
    screen.blit(imageconvoyeur, (460 , 500))
    rotated_convoyeur = pygame.transform.rotate(imageconvoyeur, 180)
    screen.blit(rotated_convoyeur, (236 , 500))
    screen.blit(rotated_convoyeur, (204 , 500))
    screen.blit(rotated_convoyeur, (172 , 500))
    screen.blit(rotated_convoyeur, (140 , 500))
    screen.blit(rotated_convoyeur, (108 , 500))
    screen.blit(resized_duo, (50 , 500))
    screen.blit(rotated_convoyeur, (76 , 500))
    rotated_convoyeur2 = pygame.transform.rotate(imageconvoyeur, 270)
    screen.blit(rotated_convoyeur2, (268 , 532))
    screen.blit(rotated_convoyeur2, (268 , 564))
    screen.blit(rotated_convoyeur2, (268 , 596))
    screen.blit(rotated_convoyeur2, (268 , 628))
    
    #sert a fair avancer premier cuivre
    if noyaux ==True:
        if x2==275 and y2 >532:
            screen.blit(resized_coper, (x2 , y2))
            y2-=vitessetapis
        else:
            y2=700
            x2=275
        #determine de quelle coter est la souri
            if x3<250:
                g=True
            if x3>350:
                d=True

        #afiche le cuivre qui vas a gauche 
        if g==True:
            x4-=vitessetapis
            screen.blit(resized_coper, (x4 , y4))
            if x4<82:
                x4=250
                y4=505
                dg=True
                g=False
        
        #afiche le cuivre qui vas a droite
        elif d==True:
            x5+=vitessetapis
            screen.blit(resized_coper, (x5 , y5))
            if x5>465:
                x5=300
                y5=505
                dd=True
                d=False
        #active le duo du milieu
        elif x3>250 and x3<350:
            dm=True


        #regle bug de non limite des flare
        if nb<0:
            nb=limit
        elif nb>limit:
            nb=limit


            
        #generation flare (decide dans quelle colone vons les flare et le nombre qu'ils sont)
        if nb < limit:
            pif=randint(1,3)
            if pif ==1 and condif1 !=True:
                condif1=True
                nb+=1
            
            elif pif ==2 and condif2 !=True:
                condif2=True
                nb+=1
            
            elif pif ==3 :
                if condif3 !=True:
                    condif3=True
                    nb+=1
    

    

        #afichage et avancement flare
        if condif1 == True:
            yf1+=vitesseflare
            screen.blit(rotated_flare, (45, yf1))
        else:
            yf1=-50
            

        if condif2 == True:
            yf2+=vitesseflare
            screen.blit(rotated_flare, (260 , yf2))
        else:
            yf2=-50
            

        if condif3 == True:
            yf3+=vitesseflare
            screen.blit(rotated_flare, (450 , yf3))
        else:
            yf3=-50
            


        #sisteme de tir
        if dg==True and condif1==True:
            screen.blit(resized_fume, (50 , 469))
            screen.blit(resized_boom, (45, yf1))
            condif1=False
            nb-=1
            score+=1
            paf=randint(1,5)
            if paf ==2:
                acuvitesse+=0.5
                paf=-555
            dg=False
    
        if dm==True and condif2==True:
            screen.blit(resized_fume, (270 , 448))
            screen.blit(resized_boom, (260, yf2))
            condif2=False
            nb-=1
            score+=1
            if paf ==2:
                acuvitesse+=0.5
                paf=-555
            dm=False

        if dd == True  and condif3==True:
            screen.blit(resized_fume, (485 , 469))
            screen.blit(resized_boom, (450, yf3))
            condif3=False
            nb-=1
            score+=1
            if paf ==2:
                acuvitesse+=0.5
                paf=-555
            dd=False

    #gere la fin du jeux
    if yf1>500 or yf2>500 or yf3>500:
        limit=-1000
        noyaux=False
        background.blit(text2, (50,300))
        noyaux=False

    
    
    



    #rien apres sa
    pygame.display.flip()
    clock.tick(60)