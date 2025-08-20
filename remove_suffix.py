# Das Programm entfernt jede Dateiendung
# Suffix bestimmen (alles nach dem letzten Punkt)
# rfind sucht von rechts nach links nach einem zeichen
# -1, wenn kein Punkt gefunden wurde
# suffix = datei[punkt_position:] -> inkl. Punkt, z.B. ".txt"

print("Willkommen! Dieses Programm entfernt die Endung von Dateinamen.")

datei = input("Bitte Dateinamen eingeben: ")

index = datei.rfind(".")  
if index != -1:
    suffix = datei[index:] 
    ohne_suffix = datei.removesuffix(suffix)
else:
    suffix = ""
    ohne_suffix = datei

print("Original:", datei)
print("Gefundene Endung:", suffix if suffix else "Keine")
print("Ohne Endung:", ohne_suffix)

