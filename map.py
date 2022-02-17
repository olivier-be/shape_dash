from random import randint
import configparser
config = configparser.ConfigParser()
config.read('.editorconfig') #ouverture ficher config
class Map:
    def __init__(self,tab):
        self.tab_str="000000"
        self.case=[0]
        self.taille_max=int(config['map']['hauteur_max'])
        self.taille=0
        self.danger_max=int(config['map']['danger_max'])
        self.danger=0
        self.case = []
        for e in range(len(tab)):
            self.tab_str+=str(ord(tab[e])*432565) # transforme les lettre en code uft8 pour réaliser une chaine de caractère
        while len(self.tab_str)<=20000:
            self.tab_str+="3"
        e=0
        while len(self.case)<1000:
            if int(self.tab_str[e])>0 and int(self.tab_str[e])<7 :
                if self.tab_str[e] == "1" or self.tab_str[e] == "2":
                    if self.taille > self.taille_max:
                        self.case.append(0)
                    else:
                        self.case.append(int(self.tab_str[e]))
                if self.tab_str[e] == "3" or self.tab_str[e] == "4":
                    if self.taille < 0:
                        self.case.append(0)
                    else:
                        self.case.append(int(self.tab_str[e]))
                if self.tab_str[e] == "5" or self.tab_str[e] == "6":
                    if self.danger > self.danger_max:
                        self.case.append(0)
                    else:
                        self.case.append(int(self.tab_str[e]))
            else:
                self.case.append(0)
            e+=1
    def __str__(self):
        print("taille:",len(self.case))
        return str(self.case)
    def nb_type_case(self):
        """ permet de connaitre le nombre de triangle , de saut , de case vide et de case sans saut
        retourn un tableau sous la forme [nbtri,nbsaut,nbvide,nb_sans_saut]"""
        nbtri=0
        nbcase_vide=0
        nbsaut=0
        nbvide=0
        for e in range (len(self.case)-1):
            if self.case[e]==5:
                nbtri+=1
            elif self.case[e]!=0 or self.case[e-1]!=self.case[e]:
                nbsaut+=1
            else:
                nbcase_vide+=1
            if self.case[e]==6:
                nbvide+=1

        return [nbtri,nbsaut,nbvide,nbcase_vide]








