"""
time.asctime() gibt immer einen String mit 24 Zeichen aus.
Www Mmm dd hh:mm:ss yyyy
Www = 3 Buchstaben für den Wochentag (z. B. Sat)

Mmm = 3 Buchstaben für den Monat (z. B. Aug)

dd = Tag, immer 2 Stellen (z. B. 7 oder 17)

hh:mm:ss = Uhrzeit, immer 8 Zeichen

yyyy = Jahr, immer 4 Zeichen
Selbst wenn der Tag einstellig ist (7 statt 17), wird vorne ein Leerzeichen ergänzt → darum bleibt die Länge konstant.
Für asctime() brauchst du ljust() nicht zwingend, weil alle Strings gleich lang sind.

Aber: Wenn du irgendwann andere Formatierungen verwendest (z. B. mit strftime("%H:%M:%S") nur die Uhrzeit), dann können die Strings unterschiedlich lang werden → da hilft ljust() wirklich.

"""
from time import asctime, sleep

print("Welcome to the Simple Clock!")
print("Press Ctrl+C to stop.\n")

while True:
    # ljust füllt mit Spaces auf, damit Reste alter Ausgabe überdeckt werden
    line = "\t" + asctime()
    print("\r" + line.ljust(40), end="", flush=True)
    sleep(1)

