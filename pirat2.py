# -*- coding: cp1250 -*-
import random, easygui

sekret = random.randint(1,99)
propozycja = 0
proba = 0
easygui.msgbox("""AHOJ! Jestem straszliwy pirat Hawaj i mam dla ciebie zagadk�! Jest ni� tajemna liczba od 1 do 99. Na jej odgadni�cie masz 6 pr�b.""")
while propozycja !=sekret and proba < 6:
    propozycja = easygui.integerbox("Jaka to liczba?")
    if propozycja < sekret:
        easygui.msgbox(str(propozycja) + " jest za ma�a, psubracie!")
    elif propozycja > sekret:
        easygui.msgbox(str(propozycja) + " jest za du�a, szczurze l�dowy!")
    proba = proba +1
if propozycja == sekret:
    easygui.msgbox("Stop! Uda�o ci si� odgadn�� moj� tajemn� liczb�!")
else:
    easygui.msgbox("Wykorzysta�e� wszystkie pr�by! Powodzenia nast�pnym razem, kole�ko! Tajemna liczba to " +str(sekret))
    
