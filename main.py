import configparser,map,algo_bot,pygame#,personnage,bot
import pygame as pg
config = configparser.ConfigParser()
config.read('.editorconfig') #ouverture ficher config
config.sections()

y=int(config["graphique"]["Dimension_y"])
x=int(config["graphique"]["Dimension_x"])

taille_case= y//11
config["map"]["case"]=str(taille_case)
config["personnage"]["taille"]=str(taille_case)
config["personnage"]["saut"]=str(taille_case*2)
vitesse=y//250
config["difficulter"]["longueur_saut"]=str(taille_case*2)
Z=map.Map("asdfqskldfjhqlksjdhfalkjshdflkjahqlkjshdfkqjshddse")
map_def=Z.get_case()
print(Z)
print(Z.nb_type_case())
print(taille_case)
print(config["personnage"]["taille"])
print(config["personnage"]["saut"])



saut_min=(algo_bot.map_bot_max(map_def,[],0))
saut_max=(algo_bot.map_bot_min(map_def,[],0))
print(len(saut_max),len(saut_min),(len(saut_max)+len(saut_min))//2)
""" 
un block = 10 pixel 
"""
print()
pygame.init()
screen = pygame.display.set_mode((int(config["graphique"]["Dimension_x"]),int(config["graphique"]["Dimension_y"])))
running = True
background=pygame.image.load(config["map"]["background"]).convert()
image = pygame.image.load(config["personnage"]["skin"]).convert()
image=pg.transform.scale(image, (int(config["personnage"]["taille"]), int(config["personnage"]["taille"])))
x_personage = taille_case*2
y_personnage =taille_case*8
print(y_personnage)
up_personnage=0
down_personnage=0
clock = pygame.time.Clock()
screen.blit(image, (x_personage,y_personnage))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        saut = True
    if pressed[pygame.K_LEFT] == False:
        saut = True
    if pressed[pygame.K_ESCAPE]:
        echap = True
    if pressed[pygame.K_ESCAPE] == False:
        echap = False
    if pressed[pygame.K_UP] and up_personnage == 0 and down_personnage==0:
        up_personnage = int(config["personnage"]["saut"])
        print("zz",up_personnage)
        y_personnage -= 1*vitesse
        up_personnage -= 1*vitesse
    if up_personnage >= 0+vitesse:
        y_personnage -= 1*vitesse
        up_personnage -= 1*vitesse
        print(up_personnage)
        if up_personnage == 0:
            down_personnage = int(config["personnage"]["saut"])
    elif up_personnage > 0:
        y_personnage -= up_personnage
        up_personnage -= up_personnage
        if up_personnage == 0:
            down_personnage = int(config["personnage"]["saut"])
    if down_personnage>=0+vitesse:
        y_personnage+=1*vitesse
        down_personnage-=1*vitesse
    elif down_personnage > 0:
        y_personnage += down_personnage
        down_personnage -= down_personnage
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    screen.blit(image, (x_personage, y_personnage))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



