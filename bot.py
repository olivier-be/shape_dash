import configparser
import sys
sys.setrecursionlimit(1000000)
config = configparser.ConfigParser()
config.read('.editorconfig') #ouverture ficher config
config.sections()


def map_bot_max(map_def, saut_bot, i):
    z=int(config["difficulter"]["longueur_saut"])
    for e in range(1,z+1):
        if len(map_def)-1>=e+i:
            if map_def[e + i] == 9:
                return saut_bot
            elif (map_def[e + i] > 0 and map_def[e + i] <= 4) or map_def[e + i] == 0:
                saut_bot.append(e)
                temp = e
                return map_bot_max(map_def, saut_bot, i + e)


def map_bot_min(map_def, saut_bot, i):
    z=int(config["difficulter"]["longueur_saut"])
    for e in range(z,0,-1):
        if len(map_def)-1>=e+i:
            if map_def[e + i] == 9:
                return saut_bot
            elif (map_def[e + i] > 0 and map_def[e + i] <= 4) or map_def[e + i] == 0:
                saut_bot.append(e)
                temp = e
                return map_bot_min(map_def, saut_bot, i + e)


def map_bot(map_def):
    saut_bot=[]
    i=0
    return(map_bot_max(map_def,saut_bot,i),map_bot_min(map_def,[],0))
