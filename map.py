import configparser
config = configparser.ConfigParser()
config.read('.editorconfig') #ouverture ficher config
class Map:
    def __init__(self,tab):
        self._tab_str= "000000"
        self._case=[0]
        self._taille_max=int(config['map']['hauteur_max'])
        self._taille=0
        self._danger_max=int(config['map']['danger_max'])
        self._danger=0
        self._case = []
        for e in range(len(tab)):
            self._tab_str+=str(ord(tab[e]) * 4325655489212302938457) # transforme les lettre en code uft8 pour réaliser une chaine de caractère
        while len(self._tab_str)<=20000:
            self._tab_str+= "3"
        e=0
        while len(self._case)<1000:
            if int(self._tab_str[e])==8 or int(self._tab_str[e])==7:

                if self._danger >= self._danger_max:
                    self._case.append(0)
                    self._danger = 0
                else:
                    self._case.append(5)
                    self._danger += 1
            if int(self._tab_str[e])>0 and int(self._tab_str[e])<7 :
                if self._tab_str[e] == "1" or self._tab_str[e] == "2":
                    self._danger = 0
                    if self._taille > self._taille_max:
                        self._case.append(0)
                    else:
                        self._case.append(int(self._tab_str[e]))
                if self._tab_str[e] == "3" or self._tab_str[e] == "4":
                    self._danger = 0
                    if self._taille < 0:
                        self._case.append(0)
                    else:
                        self._case.append(int(self._tab_str[e]))
                if self._tab_str[e] == "5" or self._tab_str[e] == "6":
                    if self._danger >= self._danger_max:
                        self._case.append(0)
                    else:
                        self._case.append(int(self._tab_str[e]))
                        self._danger+=1
            else:
                self._case.append(0)
            e+=1
        self._case.append(9)
        self._case.append(9)
        self._case.append(9)
        self._case.append(9)
    def get_case(self):
        return self._case

    def __str__(self):
        return str(self._case)
    def nb_type_case(self):
        """ permet de connaitre le nombre de triangle , de saut , de case vide et de case sans saut
        retourn un tableau sous la forme [nbtri,nbsaut,nbvide,nb_sans_saut]"""
        nbtri=0
        nbcase_vide=0
        nbsaut=0
        nbvide=0
        for e in range (len(self._case) - 1):
            if self._case[e]==5:
                nbtri+=1
            elif self._case[e]!=0 or self._case[e - 1]!=self._case[e]:
                nbsaut+=1
            else:
                nbcase_vide+=1
            if self._case[e]==6:
                nbvide+=1

        return [nbtri,nbsaut//2,nbvide,nbcase_vide]
