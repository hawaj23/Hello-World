listaImion = []
print "Wprowadz piec imion po kazdym nacisnij enter: "
for i in range(5):
    imie = raw_input()
    listaImion.append(imie)
print "Oto imie : ", listaImion
print "Zamien jedno imie."
print "Ktore imie chcesz zamienic?: "
numer = int(raw_input()) - 1
print "Jakie imie chcesz wstawic?: "
nowe = raw_input()
listaImion[numer] = nowe
print "Oto nowe imiona : ", listaImion
