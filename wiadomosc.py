import urllib2
plik = urllib2.urlopen ('http://helloworldbook2.com/data/message.txt')
wiadomosc = plik.read()
print wiadomosc
