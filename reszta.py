# -*- coding: cp1250 -*-
def Reszta(grosz50,grosz20,grosz10, grosz5):
    suma = 0.5 * grosz50 + 0.2 * grosz20 + 0.1 * grosz10 + 0.05 * grosz5
    return suma

grosz50 = int(raw_input("Prosz� wprowadzi� liczb� 50 grosz�wek: "))
grosz20 = int(raw_input("Prosz� wprowadzi� liczb� 20 grosz�wek: "))
grosz10 = int(raw_input("Prosz� wprowadzi� liczb� 10 grosz�wek: "))
grosz5 = int(raw_input("Prosz� wprowadzi� liczb� 5 grosz�wek: "))

monety = Reszta(grosz50, grosz20, grosz10, grosz5)
print "Twoje oszcz�dno�ci wynosz�: ", monety , "PLN"
