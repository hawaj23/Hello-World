# -*- coding: cp1250 -*-
import random, easygui

sekret = random.randint(1,99)
propozycja = 0
proba = 0
easygui.msgbox("""AHOJ! Jestem straszliwy pirat Hawaj i mam dla ciebie zagadkę! Jest nią tajemna liczba od 1 do 99. Na jej odgadnięcie masz 6 prób.""")
while propozycja !=sekret and proba < 6:
    propozycja = easygui.integerbox("Jaka to liczba?")
    if propozycja < sekret:
        easygui.msgbox(str(propozycja) + " jest za mała, psubracie!")
    elif propozycja > sekret:
        easygui.msgbox(str(propozycja) + " jest za duża, szczurze lądowy!")
    proba = proba +1
if propozycja == sekret:
    easygui.msgbox("Stop! Udało ci się odgadnąć moją tajemną liczbę!")
else:
    easygui.msgbox("Wykorzystałeś wszystkie próby! Powodzenia następnym razem, koleżko! Tajemna liczba to " +str(sekret))
    
