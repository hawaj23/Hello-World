# -*- coding: cp1250 -*-
print "Program Pana Hawaja konwertuj�cy temperatur� za stopni Fahrenheita na stopnie Celsjusza"
print "Wprowad� temperatur� w stopniach Fahrenheita: ",
fahrenheit = float (raw_input())
celsjusz = (fahrenheit - 32) * 5.0 /9
temperatura = int(celsjusz)
print "Taka temperatura to",
print temperatura,
print "stopni Celsjusza"
