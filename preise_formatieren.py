# Einfaches Programm zur Preisberechnung

# Einzelpreis und Anzahl
preis = 49.99
anzahl = 30

# Gesamtpreis berechnen
gesamt = preis * anzahl

# Amerikanische Schreibweise (Komma als Tausendertrenner, Punkt als Dezimalzeichen)
print(f"Amerikanisch: ${gesamt:,.2f}")

# Deutsche Schreibweise (Punkt als Tausendertrenner, Komma als Dezimalzeichen)
# Trick: Erst amerikanisch formatieren, dann Zeichen austauschen
deutsch = f"{gesamt:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f"Deutsch: {deutsch} €")

