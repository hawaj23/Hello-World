kwota=float(raw_input("Wprowadz kwote za jaka dokonales zakupow: "))
if kwota < 50:
    rachunek = kwota - (0.1 * kwota)
    print "Zosta³ ci przyznany rabat w wysokoœci 10%. Twoja kwota do zap³aty: ", + rachunek , "PLN."
else:
    rachunek = kwota - (0.2 * kwota)
    print "Zosta³ ci przyznany rabat w wysokoœci 20%. Twoja kwota do zap³aty: ", + rachunek , "PLN."
