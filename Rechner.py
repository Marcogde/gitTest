from mimetypes import init


Stundenlohn = input("Stundenlohn eintragen: ")
tag = 8 * float(Stundenlohn)
Monat = tag * 20
Netto = Monat * 0.7

print(("Dein Stundenlohn beträgt ") + str(Stundenlohn) + (" Euro"))
print(("Du verdienst " ) + str(tag)+ (" pro Tag"))
print (("Du verdienst ") + str(Monat) + (" Euro Brutto im Monat"))
print (("Dies enspricht einem Netto einkommen von ") +str(Netto) + ("Euro"))