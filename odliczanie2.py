import time
odliczanie = int(raw_input("Od ktorej sekundy odlicza�?: "))
for i in range(odliczanie,0,-1):
    print i
    time.sleep(1)
print "START!"
