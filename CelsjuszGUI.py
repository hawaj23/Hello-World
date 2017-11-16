# -*- coding: cp1250 -*-
import easygui
easygui.msgbox("Program Pana Hawaja konwertujący temperaturę za stopni Fahrenheita na stopnie Celsjusza")
fahrenheit = easygui.enterbox("Wprowadź temperaturę w stopniach Fahrenheita:")
fahrenheit2 = float(fahrenheit)
celsjusz = (fahrenheit2 - 32) * 5.0 /9
easygui.msgbox("Taka temperatura to: " + str(celsjusz) + " stopni Celsjusza")

