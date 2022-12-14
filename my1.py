import pygame
import random
import sys
pygame.init()
run = True
Menu = True
Boss =True
sc = pygame.display.set_mode((2000,1000))
sc2 = pygame.display.set_mode((1600,700))
provk11 = False
provk12 = False
provk21 = False
provk22 = False
provk31 = False
provk32 = False
provk41 = False
provk42 = False
provk51 = False
provl52 = False
provk61 = False
provk62 = False
provk71 = False
provk72 = False
provk81 = False
provk82 = False
provk91 = False
provk92 = False
provk101 = False
provk102 = False
provk111 = False
provk112 = False
provk121 = False
provk122 = False
pygame.display.set_caption("Chan vs people after 9 couples")
pygame.display.flip()
#корды перса и зомби
lol = 1
Kdshit = 1
Kdshit2 = 1
x = 100
y = 500
GunX = x
GunY = y
x1 = x
y1 = y
xZ1 = 2200
yZ1 = 400
xZ2 = 2000
yZ2 = 700
xZ3 = 2600
yZ3 = 200
xZ4 = 2400
yZ4 = 600
xZ5 = 2730
yZ5 = 450
xZ6 = 4100
yZ6 = 0
xZ7 = 5000
yZ7 = 500
xZ8 = 5500
yZ8 = 600
xZ9 = 2300
yZ9 = 300
xZ10 = 6200
yZ10 = 500
xZ11 = 7000
yZ11 = 100
xZ12 = 0
yZ12 = 0
po= 0.4
speed = 4
Перс = 1
hp = 1
Goo = 1
alala = 1
Gooo = 1
yroven = 1
nadpisX = -600
nadpisY = 300
kd = 5
shit= 1
chasti = 1
sas = 1
KROV = 2
KROV2 = 2
MOGILA = 1
jisn = 1
popa = 1
nolych = 1
Xvat = 1
rykaX = 0
rykaY = 200
popka = 1
popec = 1
snejok = 1
Kdsneg = 1
Pyshkanazemle = 1
Pyshkavrykax = 1
Kdsneg2 = 1
Kdsneg3 = 1
lak = 1
kak = 80
kak2 = 100
ZombeLed1 = 1
ZombeLed2 = 1
ZombeLed3 = 1
ZombeLed4 = 1
ZombeLed5 = 1
ZombeLed0 = 1
ZombeLed6 = 1
ZombeLed7 = 1
ZombeLed8 = 1
ZombeLed9 = 1
ZombeLed10 = 1
ZombeLed11 = 1
ZombeLed12 = 1
apa = 1
KDOR = 1
kaki = 0
asa = 1
asa2 = 1
asa3 = 1
asa4 = 1
asa5 = 1
asa6 = 1
asa7 = 1
asa8 = 1
asa9 = 1
asa10 = 1
asa11 = 1
asa12= 1
KDpay = 0
KDpay2 = 0
play = 1
Icons = 1
yesIcons = 1
noIcons = 1
ЛевоТян =2
ПравоТян = 2
НашПерсонаж = 0
xF = -50
sase = 1
ПодЗемлёй = 1
kal = 1
kal2 =1
kal3 =1
kal4 = 1
Выстрел2 = 1
Выстрел = 1
ПодЗемлёй2 = 1
asd = 1
kal5 =1
kal6 = 1
Выстрел3 = 1
ПодЗемлёй3 = 1
smert = 0
qw = 1
qw2 = 1
qw3 = 1
qw4 = 1
qw5 = 1
qw6 = 1
qw7 = 1
qw8 = 1
qw9 = 1
qw10 = 1
asd = False
qw11 = 1
vremia = 0
ololo= 1
olak = 1
opss = 0
opss2 = 0
СтенкаБосса3 =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\СтенкаБосса3.png')
win2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\win2.jpg')
hpNas = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas.png')
hpNas2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas2.png')
hpNas3 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas3.png')
hpNas4 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas4.png')
hpNas5 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas5.png')
hpNas6= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas6.png')
hpNas7 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpNas7.png')
Boss2Shit =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Boss2Shit.png')
effect2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\win.jpg')
Win =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\win.jpg') 
ЩитОгонь2 =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩитОгонь2.png')
ЩитОгонь= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩитОгонь.png')
Щит2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Щит2.png')
Dojdd = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Дождь.png')
Щит = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Щит.png')
СтенкаБосса2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\СтенкаБосса2.png')
СтенкаБосса = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\СтенкаБосса.png')
hpBossaNet = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpBossaNet.png')
hpBosssaMalo = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpBossaMalo.png')
hpBossaMenshePol = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpBossaMenshePol.png')
hpBossaPol = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpBossaPol.png')
hpBossa = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hpBossa.png')
topor3 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\topor3.png')
topor2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\topor2.png')
Boss2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Boss2.png')
lychi2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\lychi2.png')
topor= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\topor.png')
Выстреллл = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Выстрел.png') 
effect = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\effect.png') 
ranec2 =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ranec2.png') 
ranec =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ranec.png') 
Boss = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Boss.png')
ПерсонажПрямо = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПерсонажПрямо.png')
BossFight = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\BossFight.jpg')
ФонРай =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ФонРай.jpg')
BossFon = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\BossFon.jpg')
ГрязьЗемля = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ГрязьЗемля.png')
ЗомбиШахтёр =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЗомбиШахтёр.png')
Проиграл= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\proigral.png')
Флаг= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Флаг.jpg')
Таблица= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Таблица.png')
ТянЛевоКровь= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ТянЛевоКровь.png')
ТянКровь= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ТянКровь.png')
ТянЛево = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ТянЛево.png')
ПерсонажПравоМеню = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПерсонажПравоМеню.png')
ТянМеню = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ТянМеню.png')
Тян = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Тян.png')
ФонТян = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ФонТян.jpg')
ВерхТян = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ВерхТян.jpg')
НизТян = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\НизТян.jpg')
НектоТян = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\НектоТян.jpg')
Меню= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Меню.jpg')
АйконсКрас = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Айконс.jpg')
Айконс = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\АйконсНеКрас.jpg')
Плей = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Плей.jpg')
ПлейКрас = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПлейКрас.jpg')
Перезарядка =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Перезарядка.png')
Перезарядка2= pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Перезарядка2.png')
Перезарядка3 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Перезарядка3.png')
ОгоньГрязь2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ОгоньГрязь2.png')
ОгоньГрязь = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ОгоньГрязь.png')
Z0 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби.png')
Z1 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби1.png')
Z2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби2.png')
Z3 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби3.png')
Z4 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби4.png')
Z5 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби5.png')
Z6 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби6.png')
Z7 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби7.png')
Z8 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби8.png')
Z9 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби9.png')
Z10 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби10.png')
Z11 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби11.png')
Z12 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЩётЗомби12.png')
БыстрыйЗомби = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\БыстрыйЗомби.png')
СмертьЗомби = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\СмертьЗомби.png')
ЛедГрязь2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЛедГрязь2.png')
ЛедГрязь = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЛедГрязь.png')
ZombeLED =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ЛедянойЗомби.png')
sneg4 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\sneg4.png')
sneg3 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\sneg3.png')
sneg2 =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\sneg2.png')
sneg1 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\sneg1.png')
pyshka = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\pyshka.png')
lychi =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\lychi.png') 
ryka = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ryka.png') 
MOGILAA = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\MOGILA.png') 
PersKrovLevo = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПерсонажЛевоKROV.png') 
PersKrovPravo = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПерсонажПравоKROV.png') 
krov =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\krov.png') 
HP0 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hepe0.png') 
HP1 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hepe1.png') 
SHIT = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\shar.png')
HP2 =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hepe2.png')
грязь2 =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\грязь2.png')
грязь =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\грязь.png')
ФонСер =  pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ФонСер.jpg')
Go = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Go.png')
start2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\start2.png')
start =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\start.png')
HP3 =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\hepe3.png')
ПерсонажПраво =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПерсонажПраво.png')
ПерсонажЛево =pygame.image.load(r'C:\Users\PC\Documents\зомби игра\ПерсонажЛево.png')
Зомби = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Зомби.png')
Забор = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Забор.png')
Фон = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Фон.jpg')
Трещина1 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Трещина 1.jpg')
Трещина2 = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Трещина 2.png')
Дорога = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Дорога.png')
Трава = pygame.image.load(r'C:\Users\PC\Documents\зомби игра\Трава.png')
while Menu:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        sc.blit(Меню,[0,0])
        sc.blit(Айконс,[1100,300])
        if noIcons == 1:
            if play==1:
                sc.blit(Плей,[150,320])
            if play ==2:
                sc.blit(ПлейКрас,[130,300])
            if Icons == 1:
                sc.blit(Айконс,[1100,300])
            if Icons == 2:
                sc.blit(АйконсКрас,[1100,300])
            if keys[pygame.K_RIGHT]:
                 play = 1
                 Icons = 2
            if keys[pygame.K_LEFT]:
                Icons = 1
                play  = 2
        if yesIcons ==2:
            if ЛевоТян==2:
                sc.blit(НектоТян,[0,0])
            sc.blit(ФонТян,[1040,0])
            sc.blit(ФонТян,[1040,80])
            if keys[pygame.K_LEFT]:
                ЛевоТян = 1
            if keys[pygame.K_RIGHT]:
                ЛевоТян = 3
            if ЛевоТян ==3:
                sc.blit(НизТян,[0,0])
                sc.blit(ПерсонажПравоМеню,[1300,150])
            if ЛевоТян == 1:
                sc.blit(ВерхТян,[0,0])
                sc.blit(ТянМеню,[1230,150])
            if ЛевоТян == 1:
                if keys[pygame.K_SPACE]:
                    ЛевоТян = 11
                    yesIcons = 10
                    noIcons = 1
            if ЛевоТян ==3:
                if keys[pygame.K_SPACE]:
                    ЛевоТян = 10
                    yesIcons = 10
                    noIcons = 1
                
        if Icons ==1 and play == 2:
            if keys[pygame.K_SPACE]:
                aps = 2
                if ЛевоТян ==10:
                    НашПерсонаж = 1
                    Menu = False
                
                if ЛевоТян == 11:
                    НашПерсонаж = 2
                    Menu = False
                else:
                    НашПерсонаж = 2
        if Icons ==2 and play == 1:
            if yesIcons == 1:
                if keys[pygame.K_SPACE]:
                    yesIcons = 2
                    noIcons = 2
        pygame.display.update()
        sc.fill((34,139,34))    
    

while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    run =  False
    if asd:
        hp = 0
    sc = pygame.display.set_mode((2000,1000))
    if ololo ==3:
            vremia +=1
    if vremia <1500:
            sc.blit(Фон,[40,-20])
    if vremia >1500:
            sc.blit(ФонРай,[40,0])
            sc.blit(lychi,[1800,700])
            sc.blit(lychi,[1800,0])
            if x>2000:
                    run = False
    sc.blit(start,[500,215])
    sc.blit(start2,[500,605])
    if ЛевоТян == 11:
         НашПерсонаж = 2
    if ЛевоТян == 10:
        НашПерсонаж =1
    if shit == 2:
           if Kdshit <100:
                sc.blit(SHIT,[x-45,y-20])
                lol = 2
                Kdshit +=1
                KROV = 1
                KROV2 = 1
           else:
                shit = 5
                lol = 1
    if shit == 3:
         if Kdshit2 <100:
                sc.blit(SHIT,[x-45,y-20])
                lol = 2
                Kdshit2 +=1
         else:
            lol = 1
            shit = 6 
   
    if Goo == 1:
        if x>500:
            Goo = 2
            alala = 2
    if alala == 2:
        sc.blit(ФонСер,[40,-20])
        
        sc.blit(Go,[nadpisX,nadpisY])
        nolych = 2
        
        
        if nadpisX < 500:
            nadpisX +=30
        else:
            if nadpisX <1100:
                nadpisX +=10
            else:
                  nadpisX +=30
                  if nadpisX >2800:
                      alala = 3
    if keys[pygame.K_RIGHT] and x<=2500:
        if jisn ==1:
             if nolych ==1:
                sc.blit(грязь,[x-100,y+35])
        if jisn ==1:
            if nolych == 1:
                x += speed
                Перс = 1
    if keys[pygame.K_LEFT] and x>=-10:
        if jisn ==1:
            if nolych == 1:
                sc.blit(грязь,[x-100,y+35])
        if jisn == 1:
            if nolych == 1:
                x -= speed
                Перс = 2
    if keys[pygame.K_DOWN]:
        if jisn == 1:
            if nolych == 1:
                y += speed
    if keys[pygame.K_UP]:
        if jisn == 1:
            if nolych == 1:
                y -= speed
    if НашПерсонаж == 2:
        if Перс == 1:
            if KROV == 1:
                if jisn !=2:
                    sc.blit(ТянКровь,[x,y])
            else:
                sc.blit(Тян,[x,y])
            if MOGILA ==2:
                sc.blit(MOGILAA,[x,y])
        if Перс == 2:
            if KROV2 ==1:
                if jisn !=2:
                    sc.blit(ТянЛевоКровь,[x,y])
            else:
                sc.blit(ТянЛево,[x,y])
            if MOGILA == 2:
                sc.blit(MOGILAA,[x,y])
            if MOGILA == 2:
                KDOR = 2
    if НашПерсонаж == 1:
        if Перс == 1:
            if KROV == 1:
                if jisn !=2:
                    sc.blit(PersKrovPravo,[x,y])
            else:
                sc.blit(ПерсонажПраво,[x,y])
            if MOGILA ==2:
                sc.blit(MOGILAA,[x,y])
        if Перс == 2:
            if KROV2 ==1:
                if jisn !=2:
                    sc.blit(PersKrovLevo,[x,y])
            else:
                sc.blit(ПерсонажЛево,[x,y])
            if MOGILA == 2:
                sc.blit(MOGILAA,[x,y])
            if MOGILA == 2:
                KDOR = 2

    if kd ==1 or kd ==3:
        if yZ2 >200:
            yZ2 -=1
        if yZ4 <700:
            yZ4 -=1
    if kd == 0:
        kd = 5
    #Пушка
    if Pyshkanazemle == 1:
        sc.blit(pyshka,[370,220])
    if x>370 and x<470 and y>100 and y<220:
        Pyshkavrykax = 2
        Pyshkanazemle = 2
    if Pyshkavrykax == 2:
            sc.blit(pyshka,[x-40,y])
    if Pyshkavrykax == 2:
        if KDOR == 1:
            if keys[pygame.K_SPACE]:
                if KDpay <120:
                    KDpay+=1
                    
                    if Kdsneg <100:
                        Kdsneg +=1
                        if snejok == 1:
                            if Kdsneg3 !=5:
                                    Kdsneg3 +=1
                                    sc.blit(sneg1,[x+kak,y-25])
                                    sc.blit(sneg3,[x+100,y-30])
                                    Kdsneg2 = 1
                                    if kak<110:
                                        kak+=1
                            else:
                               snejok = 2
                        if snejok == 2:
                                if Kdsneg2 <5:
                                    Kdsneg2 +=1
                                    sc.blit(sneg2,[x+kak2,y+25])
                                    sc.blit(sneg4,[x+150,y])
                                    Kdsneg3 = 1
                                    if kak2<130:
                                        kak2+=1
                                else:
                                    snejok = 1
                    else:
                        if lak == 1:
                            Kdsneg3 = 1
                            Kdsneg2 = 1
                            Kdsneg = 1
                            snejok = 1
                            lak = 2
                #тут я должен задать новые ефекты,что бы переплетались,и кдснегами новые значения сделать
                        if Kdsneg <200:
                             Kdsneg +=1
                             if snejok == 1:
                                   if Kdsneg3 !=5:
                                        Kdsneg3 +=1
                                        sc.blit(sneg3,[x+100,y-30])
                                        sc.blit(sneg1,[x+kak,y-25])
                                        Kdsneg2 = 1
                                   else:
                                        snejok = 2
                                   if snejok == 2:
                                        if Kdsneg2 !=5:
                                            Kdsneg2 +=1
                                            sc.blit(sneg2,[x+kak2,y+25])
                                            sc.blit(sneg4,[x+170,y+30])
                                            Kdsneg3 = 1
                                        else:
                                            snejok = 1
                else:
                    if KDpay2 <130:
                        KDpay2 +=1
                        if KDpay2 >10:
                            sc.blit(Перезарядка,[700,660])
                        if KDpay2 >65:
                            sc.blit(Перезарядка2,[700,650])
                        if KDpay2 >115:
                            sc.blit(Перезарядка3,[700,650])
                    else:
                        KDpay = 0
                        KDpay2 = 0
                                        
  
    if alala ==3:
        ololo = 3
        sc.blit(Флаг,[xF,800])
        xF+=8
       #счёт зомб
    if asa == 1:
        if ZombeLed0 == 3:
            kaki +=1
            asa = 2
    if asa2== 1:
        if ZombeLed1 == 3:
            kaki +=1
            asa2 = 2
    if asa3 == 1:
        if ZombeLed2 == 3:
            kaki +=1
            asa3 = 2
    if asa4 == 1:
        if ZombeLed3 == 3:
            kaki +=1
            asa4 = 2
    if asa5 == 1:
        if ZombeLed4 == 3:
            kaki +=1
            asa5 = 2
    if asa6 == 1:
        if ZombeLed5 == 3:
            kaki +=1
            asa6 = 2
    if asa7 == 1:
        if ZombeLed6 == 3:
            kaki +=1
            asa7 = 2
    if asa8 == 1:
        if ZombeLed7 ==3:
            kaki !=1
            asa8 = 2
    if asa9 == 1:
        if ZombeLed8 ==3:
            kaki !=1
            asa9 = 2
    if asa10 == 1:
        if ZombeLed10 ==3:
            kaki !=1
            asa10 = 2
    if asa11 == 1:
        if ZombeLed11 ==3:
            kaki !=1
            asa11 = 2
    if asa12 == 1:
        if ZombeLed12 ==3:
            kaki !=1
            asa12 = 2
        
    if kaki ==1:
            sc.blit(Z1,[700,0])
    if kaki ==2:
            sc.blit(Z2,[700,0])
    if kaki ==3:
            sc.blit(Z3,[700,0])
    if kaki ==4:
            sc.blit(Z4,[700,0])
    if kaki ==5:
            sc.blit(Z5,[700,0])
    if kaki ==6:
            sc.blit(Z6,[700,0])
    if kaki ==7:
            sc.blit(Z7,[700,0])
    if kaki ==8:
            sc.blit(Z8,[700,0])
    if kaki ==9:
            sc.blit(Z9,[700,0])
    if kaki ==10:
            sc.blit(Z10,[700,0])
    if kaki ==11:
            sc.blit(Z11,[700,0])
    if kaki ==12:
            sc.blit(Z12,[700,0])
    
    #щит
    if alala == 3:
        if popka == 1:
            if y>200:
                y-=4
            if x<1000:
                x+=6
            else:
               Xvat = 2
               popka = 2
        if ZombeLed0 == 1:
            sc.blit(БыстрыйЗомби,[xZ6,yZ6])
        if ZombeLed0 == 2:
            sc.blit(ZombeLED,[xZ6,yZ6])
            if apa !=270:
                apa+=1
            else:
                ZombeLed0 = 3
                apa = 1
        if ZombeLed1 == 1:
            sc.blit(Зомби,[xZ1,yZ1])
        if ZombeLed1 == 2:
            sc.blit(ZombeLED,[xZ1,yZ1])
            if apa !=270:
                apa+=1
            else:
                ZombeLed1 = 3
                apa = 1
        if ZombeLed2 == 1:
            sc.blit(Зомби,[xZ2,yZ2])
        if ZombeLed2 == 2:
            sc.blit(ZombeLED,[xZ2,yZ2])
            if apa !=270:
                apa+=1
            else:
                ZombeLed2 = 3
                apa = 1
        #dgfsdgfssgpgfksgfklsgfklsgfklklgfsklgsklsgfklgflssgfldgfklsgfklslsgfkl
        if ZombeLed3 == 1:
            sc.blit(Зомби,[xZ3,yZ3])
        if ZombeLed3 == 2:
            sc.blit(ZombeLED,[xZ3,yZ3])
            if apa !=270:
                apa+=1
            else:
                ZombeLed3 = 3
                apa = 1
        if ZombeLed4==1:
            sc.blit(Зомби,[xZ4,yZ4])
        if ZombeLed4 == 2:
            sc.blit(ZombeLED,[xZ4,yZ4])
            if apa !=270:
                apa+=1
            else:
                ZombeLed4 = 3
                apa = 1
        if ZombeLed5 == 1:
            sc.blit(Зомби,[xZ5,yZ5])
        if ZombeLed5 == 2:
            sc.blit(ZombeLED,[xZ5,yZ5])
            if apa !=270:
                apa+=1
            else:
                ZombeLed5 = 3
                apa = 1
        if ZombeLed6 == 1:
            sc.blit(БыстрыйЗомби,[xZ7,yZ7])
        if ZombeLed6 == 2:
            sc.blit(ZombeLED,[xZ7,yZ7])
            if apa !=270:
                apa+=1
            else:
                ZombeLed6 = 3
                apa = 1
        if ZombeLed7 == 1:
            sc.blit(БыстрыйЗомби,[xZ8,yZ8])
        if ZombeLed7 == 2:
            sc.blit(ZombeLED,[xZ8,yZ8])
            if apa !=270:
                apa+=1
            else:
                ZombeLed7 = 3
                apa = 1
        if ПодЗемлёй ==2:
                if ZombeLed8 == 1:
                    sc.blit(ЗомбиШахтёр,[xZ9,yZ9])
                if ZombeLed8 == 2:
                    sc.blit(ZombeLED,[xZ9,yZ9])
                    if apa !=270:
                        apa+=1
                    else:
                        ZombeLed8 = 3
                        apa = 1
        if ПодЗемлёй2 ==2:
                if ZombeLed9 == 1:
                    sc.blit(ЗомбиШахтёр,[xZ10,yZ10])
                if ZombeLed9 == 2:
                    sc.blit(ZombeLED,[xZ10,yZ10])
                    if apa !=270:
                        apa+=1
                    else:
                        ZombeLed9 = 3
                        apa = 1
        if ПодЗемлёй3 ==2:
                if ZombeLed10 == 1:
                    sc.blit(ЗомбиШахтёр,[xZ11,yZ11])
                if ZombeLed10 == 2:
                    sc.blit(ZombeLED,[xZ11,yZ11])
                    if apa !=270:
                        apa+=1
                    else:
                        ZombeLed10 = 3
                        apa = 1
        if hp == 3:
            sc.blit(HP1,[-40,-80])
        if hp == 2:
            sc.blit(HP2,[-40,-80])
        if hp == 1:
            sc.blit(HP3,[-40,-80])
        if hp == 0:
            sc.blit(HP0,[-40,-80])
            sc.blit(Проиграл,[1000,500])
            sc.blit(ФонСер,[0,0])
            sase = 1
            if keys[pygame.K_CAPSLOCK]:
                Menu = True
                run = False
                
                
#зомби росподаются
        if sas !=35:
                if ZombeLed0 == 3:
                    sc.blit(СмертьЗомби,[xZ6,yZ6+60])
                    if qw == 1:
                            smert +=1
                            qw = 2
                if ZombeLed1 == 3:
                    sc.blit(СмертьЗомби,[xZ1,yZ1+60])
                    if qw2 == 1:
                            smert +=1
                            qw2 = 2
                if ZombeLed2 == 3:
                    sc.blit(СмертьЗомби,[xZ2,yZ2+60])
                    if qw3 ==1:
                            smert +=1
                            qw3 = 2
                if ZombeLed3 == 3:
                    sc.blit(СмертьЗомби,[xZ3,yZ3+60])
                    if qw4 == 1:
                            smert +=1
                            qw4 = 2
                if ZombeLed4 == 3:
                    sc.blit(СмертьЗомби,[xZ4,yZ4+60])
                    if qw5 == 1:
                            smert+=1
                            qw5 = 2
                if ZombeLed5 == 3:
                    sc.blit(СмертьЗомби,[xZ5,yZ5+60])
                    if qw6 == 1:
                            smert+=1
                            qw6 = 2
                if ZombeLed6 == 3:
                    sc.blit(СмертьЗомби,[xZ7,yZ7+60])
                    if qw7 ==1:
                            smert+=1
                            qw7 = 2
                if ZombeLed7 == 3:
                    sc.blit(СмертьЗомби,[xZ8,yZ8+60])
                    if qw8 ==1:
                            smert+=1
                            qw8 = 2
                if ZombeLed8 == 3:
                    sc.blit(СмертьЗомби,[xZ9,yZ9+60])
                    if qw9 == 1:
                            smert +=1
                            qw9 = 2
                if ZombeLed9 == 3:
                    sc.blit(СмертьЗомби,[xZ10,yZ10+60])
                    if qw10 == 1:
                            smert+=1
                            qw10 = 2
                if ZombeLed10 == 3:
                    sc.blit(СмертьЗомби,[xZ11,yZ11+60])
                    if qw11 == 1:
                            smert +=1
                            qw11 = 2

        if ZombeLed0 ==1:
            xZ6 -=5
        if  ZombeLed0 ==2:
            xZ6 -=1
        if ZombeLed1 == 1:  
             xZ1 -=2
        if ZombeLed1 == 2:
            xZ1 -=1
        if ZombeLed2 == 1:
            xZ2 -=2
        if ZombeLed2 == 2:
            xZ2 -=1
        if ZombeLed3 == 1:
            xZ3 -=2
        if ZombeLed3 == 2:
            xZ3 -=1
        if ZombeLed4==1:
            xZ4 -=2
        if ZombeLed4 == 2:
            xZ4 -=1
        if ZombeLed5 == 1:
            xZ5 -=2
        if ZombeLed5 == 2:
            xZ5 -= 1
        if ZombeLed6 ==1:
            xZ7 -=5
        if ZombeLed6 == 2:
            xZ7 -=1
        if ZombeLed7 ==1:
            xZ8 -=5
        if ZombeLed7 == 2:
            xZ8 -=1
        if ПодЗемлёй == 1:
                if ZombeLed8 == 1:
                    xZ9 -=5
               
        if ПодЗемлёй == 2:
                if ZombeLed8 == 1:
                    xZ9 -=2
                if ZombeLed8 == 2:
                    xZ9 -=1
        if ПодЗемлёй2 == 1:
                if ZombeLed9 == 1:
                    xZ10 -=5
               
        if ПодЗемлёй2 == 2:
                if ZombeLed9 == 1:
                    xZ10 -=2
                if ZombeLed9 == 2:
                    xZ10 -=1
        if ПодЗемлёй3 == 1:
                if ZombeLed10 == 1:
                    xZ11 -=5
               
        if ПодЗемлёй3 == 2:
                if ZombeLed10 == 1:
                    xZ11 -=2
                if ZombeLed10 == 2:
                    xZ11 -=1
        if yroven == 1:
            if ZombeLed1 !=3:
                if xZ1 <2000:
                    yZ2 -= 1
        if yZ2 <380:
            yroven = 2
        if yroven == 2:
            if yZ3<350:
                if yZ3<2000:
                    yZ3 +=1
            if yZ4 <700:
                if yZ4 <2000:
                    yZ4 +=1
            if yZ5 <600:
                yZ5+=1
            if yZ6 <2000:
                if yZ6 <500:
                    yZ6+=1
            if yZ8 <2000:
                if yZ8 >300:
                    yZ8-=1
    #ЗомбиПОДЗЕМНЫЙ
    if kal == 1:
            if xZ9 > x+300:
                    sc.blit(ГрязьЗемля,[xZ9,yZ9])
            else:
                    Выстрел = 2
                    ПодЗемлёй = 2
                    kal = 2
    if ZombeLed8 ==1:
            if kal2 == 1:
                    if xZ9 <1700:
                            if yZ9 >y:
                                    yZ9 -=2
                            if yZ9 <y:
                                    yZ9+=2
    if kal3 == 1:
            if xZ10 > x+300:
                    sc.blit(ГрязьЗемля,[xZ10,yZ10])
            else:
                    Выстрел2 = 2
                    ПодЗемлёй2 = 2
                    kal3 = 2
    if ZombeLed9 ==1:
            if kal4 == 1:
                    if xZ10 <1700:
                            if yZ10 >y:
                                    yZ10 -=2
                            if yZ10 <y:
                                    yZ10+=2
    if kal5 == 1:
            if xZ11 > x+300:
                    sc.blit(ГрязьЗемля,[xZ11,yZ11])
            else:
                    Выстрел3 = 2
                    ПодЗемлёй3 = 2
                    kal5 = 2
    if ZombeLed10 ==1:
            if kal5 == 1:
                    if xZ11 <1700:
                            if yZ11 >y:
                                    yZ11 -=2
                            if yZ11 <y:
                                    yZ11+=2
    if sas !=35:
            if sase ==1:
                if chasti == 1:
                    if ZombeLed1 ==1:
                       sc.blit(грязь,[xZ1,yZ1])
                    if ZombeLed1 == 2:
                        sc.blit(ЛедГрязь,[xZ1,yZ1])
                    if ZombeLed2 == 1:
                        sc.blit(грязь,[xZ2,yZ2])
                    if ZombeLed2 == 2:
                        sc.blit(ЛедГрязь,[xZ2,yZ2])
                    if ZombeLed3 == 1:
                        sc.blit(грязь,[xZ3,yZ3])
                    if ZombeLed3 == 2:
                        sc.blit(ЛедГрязь,[xZ3,yZ3])
                    if ZombeLed4 == 1:
                        sc.blit(грязь,[xZ4,yZ4])
                    if ZombeLed4 == 2:
                        sc.blit(ЛедГрязь,[xZ4,yZ4])
                    if ZombeLed5 == 1:
                        sc.blit(грязь,[xZ5,yZ5])
                    if ZombeLed5 == 2:
                        sc.blit(ЛедГрязь,[xZ5,yZ5])
                    if ZombeLed6 == 1:
                        sc.blit(ОгоньГрязь,[xZ7,yZ7])
                    if ZombeLed6 ==2:
                        sc.blit(ЛедГрязь,[xZ7,yZ7])
                    if ZombeLed7 == 1:
                        sc.blit(ОгоньГрязь,[xZ8,yZ8])
                    if ZombeLed7 == 2:
                        sc.blit(ЛедГрязь,[xZ8,xZ8])
                    if ZombeLed8 == 1:
                        sc.blit(грязь,[xZ9,yZ9])
                    if ZombeLed8 == 2:
                        sc.blit(ЛедГрязь,[xZ9,yZ9])
                    if ZombeLed9 == 2:
                        sc.blit(ЛедГрязь,[xZ10,yZ10])
                    if ZombeLed9 == 1:
                        sc.blit(грязь,[xZ10,yZ10])
                    if ZombeLed10 == 2:
                        sc.blit(ЛедГрязь,[xZ11,yZ11])
                    if ZombeLed10 == 1:
                        sc.blit(грязь,[xZ11,yZ11])
                    if hp == 0:
                             sc.blit(HP0,[-40,-80])
                             sc.blit(HP0,[-40,-80])
                             sc.blit(HP0,[-40,-80])
                             sc.blit(HP0,[-40,-80])
                             sc.blit(HP0,[-40,-80])


                    
                    if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                       sc.blit(грязь,[x-50,y])
                    chasti = 2
                elif chasti == 2:
                    if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                       sc.blit(грязь2,[x-50,y])
                    if ZombeLed10 == 2:
                       sc.blit(ЛедГрязь2,[xZ11,yZ11])
                    if ZombeLed10 == 1:
                        sc.blit(грязь2,[xZ11,yZ11]) 
                    if ZombeLed9 == 2:
                        sc.blit(ЛедГрязь2,[xZ10,yZ10])
                    if ZombeLed9 == 1:
                        sc.blit(грязь2,[xZ10,yZ10])
                    if ZombeLed8 == 2:
                        sc.blit(ЛедГрязь2,[xZ9,yZ9])
                    if ZombeLed8 == 1:
                        sc.blit(грязь2,[xZ9,yZ9])
                    if ZombeLed7 == 1:
                        sc.blit(ОгоньГрязь2,[xZ8,yZ8])
                    if ZombeLed7 == 2:
                        sc.blit(ЛедГрязь2,[xZ8,xZ8])
                    if ZombeLed6 == 1:
                       sc.blit(ОгоньГрязь2,[xZ7,yZ7])
                    if ZombeLed6 ==2:
                       sc.blit(ЛедГрязь,[xZ7,yZ7])
                    if ZombeLed5 ==1:
                       sc.blit(грязь,[xZ5,yZ5])
                    if ZombeLed5==2:
                       sc.blit(ЛедГрязь2,[xZ5,yZ5])
                    if ZombeLed4 == 1:
                       sc.blit(грязь,[xZ4,yZ4])
                    if ZombeLed4 == 2:
                        sc.blit(ЛедГрязь2,[xZ4,yZ4])
                    if ZombeLed1 ==1:
                        sc.blit(грязь2,[xZ1,yZ1])
                    if ZombeLed1 ==2:
                        sc.blit(ЛедГрязь2,[xZ1,yZ1])
                    if ZombeLed2 == 1:
                        sc.blit(грязь2,[xZ2,yZ2])
                    if ZombeLed2 == 2:
                        sc.blit(ЛедГрязь2,[xZ2,yZ2])
                    if ZombeLed3 == 1:
                        sc.blit(грязь2,[xZ3,yZ3])
                    if ZombeLed3 == 2:
                        sc.blit(ЛедГрязь2,[xZ3,yZ3])
                    chasti = 1
    provk11 = False
    provk12 = False
    provk21 = False
    provk22 = False
    provk31 = False
    provk32 = False
    provk41 = False
    provk42 = False
    provk51 = False
    provk52 = False
    provk61 = False
    provk62 = False
    provk71 = False
    provk72 = False
    provk81 = False
    provk82 = False
    provk91 = False
    provk92 = False
    provk101 = False
    provk102 = False
    provk111 = False
    provk112 = False
    provk121 = False
    provk122 = False
    if НашПерсонаж == 1:
        if ZombeLed1 !=3:
            if x in range(xZ1,xZ1 + 110) or x+ 64 in range (xZ1,xZ1 + 110):
                provk11 = True
            if y in range(yZ1,yZ1 + 159) or y+180 in range (yZ1,yZ1 + 159):
                provk12 = True
        if ZombeLed2 !=3:
            if x in range(xZ2,xZ2 + 110) or x+ 64 in range (xZ2,xZ2 + 110):
                provk21 = True
            if y in range(yZ2,yZ2 + 159) or y+180 in range (yZ2,yZ2 + 159):
                provk22 = True
        if ZombeLed3 !=3:
            if x in range(xZ3,xZ3 + 110) or x+ 64 in range (xZ3,xZ3 + 110):
                provk31 = True
            if y in range(yZ3,yZ3 + 159) or y+180 in range (yZ3,yZ3 + 159):
                provk32 = True
        if ZombeLed4 !=3:
            if x in range(xZ4,xZ4 + 110) or x+ 64 in range (xZ4,xZ4 + 110):
                provk41 = True
            if y in range(yZ4,yZ4 + 159) or y+180 in range (yZ4,yZ4 + 159):
                provk42 = True
        if ZombeLed5 !=3:
            if x in range(xZ5,xZ5 + 110) or x+ 64 in range (xZ5,xZ5 + 110):
                provk51 = True
            if y in range(yZ5,yZ5 + 159) or y+180 in range (yZ5,yZ5 + 159):
                provk52 = True
        if ZombeLed0 !=3:
            if x in range(xZ6,xZ6 + 110) or x+ 64 in range (xZ6,xZ6 + 110):
                provk61 = True
            if y in range(yZ6,yZ6 + 159) or y+180 in range (yZ6,yZ6 + 159):
                provk62 = True
        if ZombeLed6 !=3:
            if x in range(xZ7,xZ7 + 110) or x+ 64 in range (xZ7,xZ7 + 110):
                provk71 = True
            if y in range(yZ7,yZ7 + 159) or y+180 in range (yZ7,yZ7 + 159):
                provk72 = True
        if ZombeLed7 !=3:
            if x in range(xZ8,xZ8 + 110) or x+ 64 in range (xZ8,xZ8 + 110):
                provk81 = True
            if y in range(yZ8,yZ8 + 159) or y+180 in range (yZ8,yZ8 + 159):
                provk82 = True
        if ZombeLed8 !=3:
            if x in range(xZ9,xZ9 + 110) or x+ 64 in range (xZ9,xZ9 + 110):
                provk91 = True
            if y in range(yZ9,yZ9 + 159) or y+180 in range (yZ9,yZ9 + 159):
                provk92 = True
        if ZombeLed9 !=3:
            if x in range(xZ10,xZ10 + 110) or x+ 64 in range (xZ10,xZ10 + 110):
                provk101 = True
            if y in range(yZ10,yZ10 + 159) or y+180 in range (yZ10,yZ10 + 159):
                provk102 = True
        if ZombeLed10 !=3:
            if x in range(xZ11,xZ11 + 110) or x+ 64 in range (xZ11,xZ11 + 110):
                provk111 = True
            if y in range(yZ11,yZ11 + 159) or y+180 in range (yZ11,yZ11 + 159):
                provk112 = True



    if НашПерсонаж == 2:
        if ZombeLed1 !=3:
            if x in range(xZ1,xZ1 + 110) or x+ 100 in range (xZ1,xZ1 + 110):
                provk11 = True
            if y in range(yZ1,yZ1 + 159) or y+159 in range (yZ1,yZ1 + 159):
                provk12 = True
        if ZombeLed2 !=3:
            if x in range(xZ2,xZ2 + 110) or x+ 100 in range (xZ2,xZ2 + 110):
                provk21 = True
            if y in range(yZ2,yZ2 + 159) or y+159 in range (yZ2,yZ2 + 159):
                provk22 = True
        if ZombeLed3 !=3:
            if x in range(xZ3,xZ3 + 110) or x+ 100 in range (xZ3,xZ3 + 110):
                provk31 = True
            if y in range(yZ3,yZ3 + 159) or y+159 in range (yZ3,yZ3 + 159):
                provk32 = True
        if ZombeLed4 !=3:
            if x in range(xZ4,xZ4 + 110) or x+ 100 in range (xZ4,xZ4 + 110):
                provk41 = True
            if y in range(yZ4,yZ4 + 159) or y+159 in range (yZ4,yZ4 + 159):
                provk42 = True
        if ZombeLed5 !=3:
            if x in range(xZ5,xZ5 + 110) or x+ 100 in range (xZ5,xZ5 + 110):
                provk51 = True
            if y in range(yZ5,yZ5 + 159) or y+159 in range (yZ5,yZ5 + 159):
                provk52 = True
        if ZombeLed0 !=3:
            if x in range(xZ6,xZ6 + 110) or x+ 100 in range (xZ6,xZ6 + 110):
                provk61 = True
            if y in range(yZ6,yZ6 + 159) or y+159 in range (yZ6,yZ6 + 159):
                provk62 = True
        if ZombeLed6 !=3:
            if x in range(xZ7,xZ7 + 110) or x+ 100 in range (xZ7,xZ7 + 110):
                provk71 = True
            if y in range(yZ7,yZ7 + 159) or y+159 in range (yZ7,yZ7 + 159):
                provk72 = True
        if ZombeLed7 !=3:
            if x in range(xZ8,xZ8 + 110) or x+ 100 in range (xZ8,xZ8 + 110):
                provk81 = True
            if y in range(yZ7,yZ7 + 159) or y+159 in range (yZ8,yZ8 + 159):
                provk82 = True
        if ZombeLed8 !=3:
            if x in range(xZ9,xZ9 + 110) or x+ 100 in range (xZ9,xZ9 + 110):
                provk91 = True
            if y in range(yZ9,yZ9 + 159) or y+159 in range (yZ9,yZ9 + 159):
                provk92 = True
        if ZombeLed9 !=3:
            if x in range(xZ10,xZ10 + 110) or x+ 100 in range (xZ10,xZ10 + 110):
                provk101 = True
            if y in range(yZ10,yZ10 + 159) or y+159 in range (yZ10,yZ10 + 159):
                provk102 = True
        if ZombeLed10!=3:
            if x in range(xZ11,xZ11 + 110) or x+ 100 in range (xZ11,xZ11 + 110):
                provk111 = True
            if y in range(yZ11,yZ11 + 159) or y+159 in range (yZ11,yZ11 + 159):
                provk112 = True


        


    #сопрекосновение пушкой к зомби
    if KDpay !=150:
        if keys[pygame.K_SPACE]:
                if KDpay <120:
                     if ZombeLed0 !=3:
                         if x+300 in range(xZ6,xZ6 + 110) or x+100 in range (xZ6,xZ6 + 110):
                             ZombeLed0 = 2
                         if x==xZ6 -300:
                             if y in range(yZ6,yZ6 + 159):
                                 ZombeLed0 = 2
                     if ZombeLed1 !=3:
                         if x+300 in range(xZ1,xZ1 + 110) or x+100 in range (xZ1,xZ1 + 110):
                             ZombeLed1 = 2
                         if x==xZ1 -300:
                             if y in range(yZ1,yZ1 + 159):
                                 ZombeLed1 = 2
                     if ZombeLed2 !=3:
                         if x+300 in range(xZ2,xZ2 + 110) or x+100 in range (xZ2,xZ2 + 110):
                             ZombeLed2 = 2
                         if x==xZ2 -300:
                             if y in range(yZ2,yZ2 + 159):
                                 ZombeLed2 = 2
                     if ZombeLed3 !=3:
                         if x+300 in range(xZ3,xZ3 + 110) or x+100 in range (xZ3,xZ3 + 110):
                             ZombeLed3 = 2
                         if x==xZ3 -300:
                             if y in range(yZ3,yZ3 + 159):
                                 ZombeLed3 = 2
                     if ZombeLed4 !=3:
                         if x+300 in range(xZ4,xZ4 + 110) or x+100 in range (xZ4,xZ4 + 110):
                             ZombeLed4 = 2
                         if x==xZ4 -300:
                             if y in range(yZ4,yZ4+ 159):
                                 ZombeLed4 = 2
                     if ZombeLed5 !=3:
                         if x+300 in range(xZ5,xZ5 + 110) or x+100 in range (xZ5,xZ5 + 110):
                             ZombeLed5 = 2
                         if x==xZ5 -300:
                             if y in range(yZ5,yZ5 + 159):
                                 ZombeLed5 = 2
                     if ZombeLed6 !=3:
                         if x+300 in range(xZ7,xZ7 + 110) or x+100 in range (xZ7,xZ7 + 110):
                             ZombeLed6 = 2
                         if x==xZ7 -300:
                            if y in range(yZ7,yZ7 + 159):
                                 ZombeLed6 = 2
                     if ZombeLed7 !=3:
                         if x+300 in range(xZ8,xZ8 + 110) or x+100 in range (xZ8,xZ8 + 110):
                             ZombeLed7 = 2
                         if x==xZ8 -300:
                            if y in range(yZ8,yZ8 + 159):
                                 ZombeLed7 = 2
                     if Выстрел == 2:
                             if ZombeLed8 !=3:
                                 if x+300 in range(xZ9,xZ9 + 110) or x+100 in range (xZ9,xZ9 + 110):
                                     ZombeLed8 = 2
                                 if x==xZ9 -300:
                                    if y in range(yZ9,yZ9 + 159):
                                         ZombeLed8 = 2
                     if Выстрел2 == 2:
                             if ZombeLed9 !=3:
                                 if x+300 in range(xZ10,xZ10 + 110) or x+100 in range (xZ10,xZ10 + 110):
                                     ZombeLed9 = 2
                                 if x==xZ10 -300:
                                    if y in range(yZ10,yZ10 + 159):
                                         ZombeLed9 = 2
                     if Выстрел3 == 2:
                             if ZombeLed10 !=3:
                                 if x+300 in range(xZ11,xZ11 + 110) or x+100 in range (xZ11,xZ11 + 110):
                                     ZombeLed10 = 2
                                 if x==xZ11 -300:
                                    if y in range(yZ11,yZ11 + 159):
                                         ZombeLed10 = 2
   
   
        





       



        
    if lol == 1:
        if shit == 6:
            if provk11 and provk12 or provk21 and provk22 or provk31 and provk32 or provk41 and provk42 or provk51  and provk52 or provk61 and provk62 or provk71 and provk72 or provk81 and provk82 or provk91 and provk92 or provk101 and provk102 or provk111 and provk112 or provk121 and provk122:

                hp = 0
                asd = True
                sas = 35
                MOGILA = 2
                jisn = 1
                
        if shit == 5:
            if provk11 and provk12 or provk21 and provk22 or provk31 and provk32 or  provk41 and provk42 or provk51  and provk52 or provk61 and provk62 or provk71 and provk72 or provk81 and provk82 or provk91 and provk92 or provk101 and provk102 or provk111 and provk112 or provk121 and provkl22:
                hp = 3
                shit = 3
        else:
            if sas == 1:
                  if provk11 and provk12 or provk21 and provk22 or provk31 and provk32 or provk41 and provk42 or provk51 and provk52 or provk61 and provk62 or provk71 and provk72 or provk81 and provk82 or provk91 and provk92 or provk101 and provk102 or provk111 and provk112 or provk121 and provk122:
                     hp = 2
                     shit = 2
 
    
    
    if alala == 3:
        if popec == 1:
            sc.blit(lychi,[x-220,y-100])
    if Xvat == 2:
        sc.blit(ryka,[rykaX,rykaY])
        if rykaX<x-380:
                rykaX +=9
                rykaY -=5
        else:
            if rykaX>-250:
                rykaX -=24
                rykaY +=14
                x -=18
                y+=10
            else:
                Xvat = 1
                nolych = 1
                popec = 2
     #если зомби зайдут далеко
    if xZ1 <-70 or xZ2<-70 or xZ4<-70 or xZ5<-70 or xZ6<-70 or xZ7<-70 or xZ8<-70 or xZ9<-70 or xZ1<-70 or xZ11<-70 or xZ12<-70:
       sc.blit(ФонСер,[0,0])
       sc.blit(Проиграл,[-300,-100])
       asd = 2
    if asd == 1:
            sc.blit(Таблица,[0,100])
    
    if hp == 0:
             sc.blit(HP0,[-40,-80])
             sc.blit(HP0,[-40,-80])
             sc.blit(HP0,[-40,-80])
             sc.blit(HP0,[-40,-80])
             sc.blit(HP0,[-40,-80])
    if sas == 35:
            sc.blit(MOGILAA,[x,y])

    kd -=1
    pygame.display.update()
    sc.fill((34,139,34))
while Boss:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        sc.blit(BossFon,[0,50])
        sc.blit(BossFight,[0,0])
        if olak == 1:
                olak = 2
                speed = 4
                lol = 1
                Kdshit = 1
                Kdshit2 = 1
                x = 0
                y = 400
                GunX = x
                GunY = y
                x1 = x
                y1 = y
                xZ1 = 2200
                yZ1 = 400
                xZ2 = 2000
                yZ2 = 700
                xZ3 = 2600
                yZ3 = 200
                xZ4 = 2400
                yZ4 = 600
                xZ5 = 2730
                yZ5 = 450
                xZ6 = 4100
                yZ6 = 0
                xZ7 = 5000
                yZ7 = 500
                xZ8 = 5500
                yZ8 = 600
                xZ9 = 2300
                yZ9 = 300
                xZ10 = 6200
                yZ10 = 500
                xZ11 = 7000
                yZ11 = 100
                xZ12 = 0
                yZ12 = 0
                po= 0.4
                speed = 5
                Перс = 1
                hp = 1
                Goo = 1
                alala = 1
                Gooo = 1
                yroven = 1
                nadpisX = -600
                nadpisY = 300
                kd = 5
                shit= 1
                chasti = 1
                sas = 1
                KROV = 2
                KROV2 = 2
                MOGILA = 1
                jisn = 1
                popa = 1
                nolych = 1
                Xvat = 1
                rykaX = 0
                rykaY = 200
                popka = 1
                popec = 1
                snejok = 1
                Kdsneg = 1
                Pyshkanazemle = 1
                Pyshkavrykax = 1
                Kdsneg2 = 1
                Kdsneg3 = 1
                lak = 1
                kak = 80
                kak2 = 100
                ZombeLed1 = 1
                ZombeLed2 = 1
                ZombeLed3 = 1
                ZombeLed4 = 1
                ZombeLed5 = 1
                ZombeLed0 = 1
                ZombeLed6 = 1
                ZombeLed7 = 1
                ZombeLed8 = 1
                ZombeLed9 = 1
                ZombeLed10 = 1
                ZombeLed11 = 1
                ZombeLed12 = 1
                apa = 1
                KDOR = 1
                kaki = 0
                asa = 1
                asa2 = 1
                asa3 = 1
                asa4 = 1
                asa5 = 1
                asa6 = 1
                asa7 = 1
                asa8 = 1
                asa9 = 1
                asa10 = 1
                asa11 = 1
                asa12= 1
                KDpay = 0
                KDpay2 = 0
                play = 1
                Icons = 1
                yesIcons = 1
                noIcons = 1
                ЛевоТян =2
                ПравоТян = 2
                НашПерсонаж = 1
                xF = -50
                sase = 1
                ПодЗемлёй = 1
                kal = 1
                kal2 =1
                kal3 =1
                kal4 = 1
                Выстрел2 = 1
                Выстрел = 1
                ПодЗемлёй2 = 1
                asd = 1
                kal5 =1
                kal6 = 1
                Выстрел3 = 1
                ПодЗемлёй3 = 1
                smert = 0
                qw = 1
                qw2 = 1
                qw3 = 1
                qw4 = 1
                qw5 = 1
                qw6 = 1
                qw7 = 1
                qw8 = 1
                qw9 = 1
                qw10 = 1
                asd = False
                qw11 = 1
                vremia = 0
                ololo= 1
                olak = 2
                olak = 2
                xB = 2150
                yB = 1000
                Ytiaga = 1
                papa = 0
                pipi = 0
                x11 = 4000
                y11 = 4000
                pup = 1
                pup2 = 2
                pf = False
                pff = False
                x12 = 4000
                y12 = 4000
                pipii = 1
                palka = 1
                palka2 = 1
                palka3 = 1
                kakal = 1
                kakal2 =1
                pup3 = 1
                pup4 =1
                x13 = 4000
                y13 = 4000
                arq = 0
                Kalash = 1
                xB2 = 1600
                yB2 = 500
                papo = 0
                papo2 = 0
                papo3 = 0
                papo4 = 0
                tab = False
                tab2 = False
                afs = 1
                hpBossaa = 2
                hpBossaaPol = 1
                hpBossaaMenshePol = 1
                hpBossaaMalo = 1
                hpBossaaNet = 1
                Bis = 0
                papo5 =0
                papo6 = 0
                papo7 = 0
                papo8 = 0
                papo9 = 0
                papo10 = 0
                papo11 =0
                papo12 = 0
                Bis2 = 0
                Bis3 = 0
                popo13 = 0
                popo14 = 0
                popo15 = 0
                popo16 = 0
                apap = 0
                KDD = False
                KDD2 = False
                xS = 1400
                yS = 300
                pqp = 1
                gaw = 1
                gaw2 = 1
                STENA = 1
                qr = 0
                xD = 0
                yD = -1998
                xD2 = 388
                yD2 = -1998
                xD3 = 0
                yD3 = -1350
                xD4 = 388
                yD4 = -1350
                Dojd = 1
                stenaa = 1
                hgg = 1
                opa = 1
                SHITS = 1
                adf = 1
                HBP = 1
                boSS = 1
                apip = 1
                adf2 =1
                afd = 1
                Kalashh = 1
                apff = 0
                KalaH = 0
                apq = 1
                apq2 = 1
                KalasH = 1
                pla = 1
                kka = 1
                agf = 1
                q1 = 0
                q2 = 0
                q3 = 0
                q4 = 0
                q5 = 0
                q6 = 0
                q7 = 0
                w1 = 0
                w2 = 0
                w3 = 0
                w4 = 0
                w5 = 0
                w6 = 0
                w7 = 0
                KDDD = False
                KDDD2 = False
                hpn = 0
                ddf =1
                pfs = 1
                APas = 1
        if boSS == 1:
                sc.blit(Boss,[xB,yB])
        if boSS ==2:
                sc.blit(Boss2,[xB,yB])
        if ddf == 2:
                 sc.blit(Boss2Shit,[xB-70,yB-50])
        if Dojd == 3:
                if qr <130:
                        qr +=1
                else:
                        sc.blit(Dojdd,[xD,yD])
                        sc.blit(Dojdd,[xD2,yD2])
                        sc.blit(Dojdd,[xD3,yD3])
                        sc.blit(Dojdd,[xD4,yD4])
                        yD+=20
                        yD2 +=20
                        yD3 +=20
                        yD4 +=20
        if НашПерсонаж ==1:
                sc.blit(ПерсонажПрямо,[x,y])
        if xD>1300:
                if apq ==1:
                        sc.blit(topor,[755,35])
                        sc.blit(lychi2,[700,0])
                if x>700 and  x<740 and y<100 and y>0:
                        apq = 2
                        KalasH = 12
        else:
                if apq2 == 1:
                        sc.blit(Щит,[755,35])
                        sc.blit(lychi2,[700,0])
                if x>700 and  x<740 and y<100 and y>0:
                        KalasH = 2
                        apq2 = 2
                
        if Ytiaga == 2:
                y +=9
        
        
        else:
                sc.blit(MOGILAA,[x,y])
                y+=3
        #089898395385393893893bxvfksdhflslmldfsmldgfslmldgml
        if Ytiaga ==2:
                if НашПерсонаж == 1:
                        if keys[pygame.K_SPACE]:
                                y-=14
                                papa +=2
                                if papa <10:
                                        sc.blit(ranec,[x-50,y+30])
                                else:
                                        if papa<20:
                                               sc.blit(ranec2,[x-50,y+30])
                                        else:
                                                papa = 0
        #СМЕРТЬ ОТ БОСА ЗПЫХВАЫХЪПЖАЫПЖАХЫЖХВПАЫЪХВАФЫДЗРВАЛЫЦЩРХАЛЫЦХЗРДЪЫЗРДЪЗАХЫДРХЫДРАЫРАЫПРАЫРАЫЗРАХДЫЪЗЖАХД
        if pfs == 1:
                if x>400:
                        pfs = 2
                else:
                        Ytiaga = 2
                        y-=9

                                
        
        if Ytiaga == 2:
                pipi = 1
        if xB >1400:
                xB-=2
        if pipi == 1:
                afs = 2
                if yB >300:
                        yB -=2
                        if agf == 1:
                                sc.blit(effect,[xB,yB+100])
                                agf = 2
                        elif agf ==2:
                                sc.blit(effect2,[xD,yB+100])
                                agf = 1
                else:
                        if palka2 == 1:
                                x11 = 1400
                                y11 = 400
                                palka2 = 2
                        pipi = 2
                

        
                                
                        

        if pipi == 2:
                stenaa = 2 
                
                if xS>780:
                        xS -=10
                else:
                        STENA = 2
                        gaw = 2
                if yS>0:
                        yS-=10
                else:
                        gaw2 = 2
        if apip == 1:
                if stenaa == 2:
                        if hgg == 1:
                                sc.blit(СтенкаБосса2,[xS,yS])
                                                                                #540045903459409-9
        if APas == 2:
                sc.blit(СтенкаБосса3,[xS,yS])
        
                        
                        
                
        if pipi == 2:
                if arq <50:
                        if gaw == 2 and gaw2 == 2:
                                sc.blit(Выстреллл,[x11,y11])
                                arq +=1
                                x11 -=3
        if pipi == 2:
                if gaw == 2 and gaw2 == 2:
                        sc.blit(Выстреллл,[x11,y11])
                        x11 -= 13
                        pipii = 2
        if pipii == 2:
                if xB>1100:
                        xB-=2
                else:
                        pup = 2
                if yB>100:
                        yB-=2
                else:
                        pup2 = 2
        

        
        if pup ==2 and pup2 == 2:
                 if palka ==1:
                         x12 = 1200
                         y12 = 200
                         palka = 2
                         
                 sc.blit(Выстреллл,[x12,y12])
                 kakal = 2
                 x12-=13
                 if x12>360:
                         if y12 < y:
                                        y12+=6.5
                         if y12 >y:
                                         y12 -=6.5
        #463o6kdhkpkdgpkdkfkjdvflhjdgflh;dgf.hmk,f.xvgc,mnglhdl;fj,gjlgf;gfj;gfjd;gfj;lgfj
        if yD3>1300:
                 if kka==1:
                         sc.blit(topor,[755,35])
                         sc.blit(lychi2,[700,0])
                 if x>700 and  x<740 and y<100 and y>0:
                          pla = 2
                          kka = 2
        if kka == 2:
                sc.blit(topor,[x+35,y])
        if kakal == 2:
                if xB<1600:
                        xB+=8
                if yB<500:
                        yB+=5
                
        if kakal ==2:
                if xB<1600:
                        xB+=2
                else:
                        pup3 = 2
                if yB<360:
                        yB+=2
                else:
                        
                        pup4 = 2
        if pup3 ==2 and pup4 == 2:
                kakal = 5
                if palka3 ==1:
                         x13 = 1600
                         y13 = 500
                         boSS = 2
                         palka3 = 2
                         
                sc.blit(Выстреллл,[x13,y13])
                x13-=11
                if x13>500:
                        if y13 < y:
                                 y13+=6.5
                        if y13 >y:
                                         y13 -=6.5
                        kakal2 = 2
        if MOGILA == 2:
                sc.blit(MOGILAA,[x,y])
        
                 
                
        if x11  >x -100:
                if x>x11 and x<x11+169 and y>y11 and y<y11+147: 
                        НашПерсонаж = 2
                        MOGILA = 2
        else:
                if x11<-50:
                        x11 = -2222
        if x12 >x - 100:
                if x>x12 and x<x12+169 and y>y12 and y<y12+147: 
                        НашПерсонаж = 2
                        MOGILA = 2
        else:
                if x12<-50:
                        x12 = -3131
        if x13 >x - 100:
                if x>x13 and x<x13+169 and y>y13 and y<y13+147: 
                        НашПерсонаж = 2
                        MOGILA = 2
        else:
                if x13<-50:
                        x13 = -2222
        if yD<1300:
                if SHITS !=2:
                        if yD3+648>y:
                                        sc.blit(Щит,[3000,3000])
        else:
                 
                adf2 = 1
                adf = 2
                Kalash = 6
                SHITS = 3
        if adf2 ==1:
                
                if x>700 and  x<740 and y<100 and y>0:
                      Kalash = 12
        if adf == 2:                
                if x>760:
                        if keys[pygame.K_TAB]:
                                apip = 2
                                APas= 2
                                apff +=1
                                if apff <30:
                                        Kalash = 12
                                else:
                                        Kalash= 3
                                        if apff<60:
                                                Kalash = 4
                                                if apff<80:
                                                        apff = 1
                                
        if yD3>1400:
                if x>700 and  x<740 and y<100 and y>0:
                        Kalash = 17
        #53q2tlwgpfpfpfghpgfplfeplpgflpgfekehjdpfhllh;dgelhndrgelhjrgelphjgfp;hnjldfenj
       
        if hpBossaaNet == 8:
                sc.blit(Win,[0,500])
                sc.blit(Win,[1270,500])
                boSS = 3
                               
        
                                
                                
        #билет на держания оружия
        if Kalash == 2:
                sc.blit(Щит,[4224,2430])
        if Kalashh == 99:
                sc.blit(topor,[4224,4224])                                      #привет пашаЯнесдался
        if Kalash == 3:
                sc.blit(topor2,[4224,2430])
        if Kalash == 4:
                sc.blit(topor3,[2415,4230])
        if kakal == 2:
                HPB = 2
        if pla == 1:
                if KalasH == 2:
                        sc.blit(Щит,[x+15,y+30])
        if KalasH == 12:
                sc.blit(topor,[3230,2330])                                      #привет пашаЯнесдался
        if KalasH == 3:
                sc.blit(topor2,[x+15,y+30])
        if KalasH == 4:
                sc.blit(topor3,[x+15,y+30])
        if HBP ==2:
                if hpBossaa == 2:
                        sc.blit(hpBossa,[1400,0])
                if hpBossaaPol == 2:
                        sc.blit(hpBossaPol,[1400,0])
                if hpBossaaMenshePol == 2:
                        sc.blit(hpBossaMenshePol,[1400,0])
                if hpBossaaMalo == 2:
                        sc.blit(hpBosssaMalo,[1400,0])
                if hpBossaaNet == 2:
                        sc.blit(hpBossaNet,[1400,0])
                        sc.blit(win2,[0,0])
     
        #розобратся почему после финального замаха,не пропадают все хп а так же само остаётся немного
        #оружие
        if kakal2 == 2:
                sc.blit(Щит,[755,35])
                sc.blit(lychi2,[700,0])
                Dojd = 2
       
        if kakal == 5:
                if keys[pygame.K_CAPSLOCK]:
                         if yD3+648>y:
                                 SHITS = 2
                         if SHITS==1:
                                 sc.blit(Щит2,[x-120,y-100])
                                 kalash = 5
                         Dojd = 3
                else:
                        if adf == 2:
                                kalash = 2
        if keys[pygame.K_CAPSLOCK]:
                KalasH = 5
                if SHITS==2:
                        if opa == 1:
                               sc.blit(ЩитОгонь,[x-170,y-70])
                               opa = 2
                        elif opa ==2:
                                sc.blit(ЩитОгонь2,[x-170,y-70])
                                opa = 1
        else:
                if adf == 2:
                        Kalash = 2                        
        if yD>1400:
                SHITS = 1
        if adf == 1:
                if x>700 and  x<740 and y<100 and y>0:
                        Kalash = 12
                        kakal2 = 5
                        adf = 2
        if x+150 in range(xB2,xB2 + 234) or x+ 100 in range (xB2,xB2 + 234):
                KDD = True
        if y in range(yB2,yB2 + 348) or y+159 in range (yB2,yB2 + 348):
                KDD2 = True
        #dgfskpogfspkdgfspkdgfspsdgfkdfpkcdfsphdpfskhpdfsklhphflsphfdlphdsdhfspldhfspldhfsplhfdsldhfsdhflsphfldplhf05o50y905g5940y59370590y9 754030b35ub7= u59u35 3 5 53 539u57 9  5749-u5749u579u574 5794u 579- 9-9-349-5749-u5749-u
        if ddf == 1:
                if x>1200:
                        hpn = 1
                        ddf = 2
        if ddf == 2:
                if xB>1100:
                        xB-=3
                if yB<300:
                        yB-=1

                        
       
                               
        if hpn == 1:
                  sc.blit(hpNas,[0,0])
        if hpn == 2:
                  sc.blit(hpNas2,[0,0])
        if hpn == 3:
                  sc.blit(hpNas3,[0,0])
        if hpn == 4:
                  sc.blit(hpNas4,[0,0])
        if hpn == 5:
                  sc.blit(hpNas5,[0,0])
        if hpn == 6:
                  sc.blit(hpNas6,[0,0])
        if hpn == 7:
                  sc.blit(hpNas7,[0,0])
        if x>1200:
                if x+100 in range(xB2,xB2 + 234) or x+ 100 in range (xB2,xB2 + 234):
                        KDDD = True
                else:
                        KDDD = False
                                
                if y in range(yB2,yB2 + 348) or y+159 in range (yB2,yB2 + 348):
                        KDDD2 = True
                else:
                        KDDD2 = False
        if KDDD and KDDD2:
                w1 = 0
                w2 =0
                w3 = 0
                w4 = 0
                w5 = 0
                w6 = 0
                w7 = 0
                if q1 <100:
                        q1+=1

                else:
                        
                        hpn = 2
                        if q2 <100:
                                q2+=1
                        else:
                                hpn = 3
                                if q3 <100:
                                        q3 +=1
                                else:
                                        hpn = 4
                                        if q4 <100:
                                                q4+=1
                                        else:
                                                hpn = 5
                                                if q5 <100:
                                                        q5+=1
                                                else:
                                                        hpn = 6
                                                        if q6 <30:
                                                                q6 +=1
                                                        else:
                                                                hpn = 7
        else:
                q1 = 0
                q2 = 0
                q3 = 0
                q4 = 0
                q5 = 0
                q6 = 0
                q7 = 0
                if hpn  ==2:
                        
                        if w1<30:
                                w1+=1
                        else:
                                hpn = 1
                if hpn  ==3:
                         if w2<30:
                                 w2+=1
                         else:
                                hpn = 2
                if hpn  ==4:
                        if w3<30:
                                w3+=1
                        else:
                                hpn = 3
                if hpn  ==5:
                        if w4<30:
                                w4+=1
                        else:
                                hpn = 4
                if hpn  ==6:
                        if w5<30:
                                w5+=1
                        else:
                                hpn = 5
                if hpn  ==7:
                        if w6<30:
                                w6+=1
                        else:
                                hpn = 6
                                
                                
                                
                                
                                
                                                
                        
                        
        
        if НашПерсонаж ==1:
                if keys[pygame.K_RIGHT] and x<400:
                        sc.blit(ПерсонажПраво,[x,y])
                        x += speed
                if apip == 1:
                        if keys[pygame.K_RIGHT] and x>=400 and x<=800:
                                sc.blit(ПерсонажПраво,[x,y])
                                x += speed
                                Ytiaga = 2
                if apip == 2:
                        HBP = 2
                        if keys[pygame.K_RIGHT]:
                                sc.blit(ПерсонажПраво,[x,y])
                                x += speed
                                Ytiaga = 2
                if keys[pygame.K_LEFT] and x>0:
                        sc.blit(ПерсонажЛево,[x,y])
                        x -= speed  
        if KDD and KDD2:
              
                if keys[pygame.K_TAB]:
                        kka = 1
                        if hpBossaa ==2:
                                KalasH = 12

                                if papo <30:
                                        papo +=1
                                else:
                                        KalasH = 12
                                        
                                        if papo2 <30:
                                                papo2 +=1
                                        else:
                                                KalasH =3
                                                
                                                if papo3 <30:
                                                        papo3+=1
                                                else:
                                                        KalasH = 4
                                                        
                                                        if papo4<30:
                                                                papo4+=1
                                                        else:
                                                                KalasH = 1
                                                                hpBossaaPol = 2
                                                                hpBossaa = 1
                                                                                                                                                                                                                                          
                        if hpBossaaPol == 2:                                                                                                                                                                                                                                                                                                         
                                if Bis <50:
                                  if Bis>10 and Bis<25:
                                          sc.blit(Перезарядка,[1000,500])
                                  if Bis>25 and Bis <38:
                                          sc.blit(Перезарядка2,[1000,500])
                                  if Bis>38:
                                          sc.blit(Перезарядка2,[1000,500])
                                  Bis +=1
                                else:
                                        if hpBossaaPol ==2:
                                                KalasH = 12
                                                if papo5 <30:
                                                        papo5 +=1
                                                else:
                                                        KalasH = 12
                                                        if papo6 <30:
                                                                papo6 +=1
                                                        else:
                                                                KalasH =3
                                                                if papo7 <30:
                                                                        papo7+=1
                                                                else:
                                                                        KalasH = 4
                                                                        if papo8<30:
                                                                                papo8+=1
                                                                        else:
                                                                                KalasH = 1
                                                                                hpBossaaPol = 1
                                                                                hpBossaaMenshePol = 2
                                                                                                                                                                                                                                                                                                                                         
                        if hpBossaaMenshePol == 2:                                                                                                                                                                                                                                                                                                         
                                                if Bis2 <50:
                                                  if Bis2>10 and Bis2<25:
                                                          sc.blit(Перезарядка,[1000,500])
                                                  if Bis2>25 and Bis2 <38:
                                                          sc.blit(Перезарядка2,[1000,500])
                                                  if Bis2>38:
                                                          sc.blit(Перезарядка2,[1000,500])
                                                  Bis2 +=1
                                                else:
                                                        if hpBossaaMenshePol ==2:
                                                                KalasH = 12
                                                                if papo9 <30:
                                                                        papo9 +=1
                                                                else:
                                                                        KalasH = 12
                                                                        if papo10 <30:
                                                                                papo10 +=1
                                                                        else:
                                                                                KalasH =3
                                                                                if papo11 <30:
                                                                                        papo11+=1
                                                                                else:
                                                                                        KalasH = 4
                                                                                        if papo12<30:
                                                                                                papo12+=1
                                                                                        else:
                                                                                                KalasH = 1
                                                                                                hpBossaaPol = 1
                                                                                                hpBossaaMenshePol = 1
                                                                                                hpBossaaMalo = 2#
                        if hpBossaaMalo == 2:                                                                                                                                                                                                                                                                                                         
                                                if Bis3 <50:
                                                  if Bis3>10 and Bis3<25:
                                                          sc.blit(Перезарядка,[1000,500])
                                                  if Bis3>25 and Bis3 <38:
                                                          sc.blit(Перезарядка2,[1000,500])
                                                  if Bis3>38:
                                                          sc.blit(Перезарядка2,[1000,500])
                                                  Bis3 +=1
                                                else:
                                                        if hpBossaaMalo ==2:
                                                                KalasH = 12
                                                                if popo13 <30:
                                                                        popo13 +=1
                                                                else:
                                                                        KalasH = 12
                                                                        if popo14 <30:
                                                                                popo14 +=1
                                                                        else:
                                                                                KalasH =3
                                                                                if popo15 <30:
                                                                                       popo15+=1
                                                                                else:
                                                                                        KalasH = 4
                                                                                        if popo16<30:
                                                                                                popo16+=1
                                                                                        else:
                                                                                                KalasH = 1
                                                                                                hpBossaaPol = 1
                                                                                                hpBossaaMenshePol = 1
                                                                                                hpBossaMalo = 1
                                                                                                hpBossaaNet= 2
                else:
                        kka = 2

            

        
                        
                        


                
        

        



#сделать спрайт двух огней возле щита,и когда дойдёт дождь до конца мапы,мы вырубаем ЩИТС2 НА ЩИТ 1,И ПРИ КАПС ЛОКЕ У НАС БУДЕТ ОБЫЧНЫЙ ЩИТ
        
        pygame.display.update()
        sc.fill((34,139,34))
 



