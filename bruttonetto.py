def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    mojaCenaNetto = 10000
    print "mojaCenaNetto (wewnatrz funkcji) = ", mojaCenaNetto
    return razem

mojaCenaNetto = float(raw_input("Wprowadz cene netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, "Cena brutto = ", cenaBrutto
print "mojaCenaNetto (na zewnatrz funkcji) = ", mojaCenaNetto

