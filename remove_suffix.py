# Das Programm entfernt jede Dateiendung
# Suffix bestimmen (alles nach dem letzten Punkt)
# rfind sucht von rechts nach links nach einem zeichen
# -1, wenn kein Punkt gefunden wurde
# suffix = datei[punkt_position:] -> inkl. Punkt, z.B. ".txt"

print("Willkommen! Dieses Programm entfernt die Endung von Dateinamen.")

myFile = input("Bitte Dateinamen eingeben: ")

index = myFile.rfind(".")  
if index != -1:
	suffix = myFile[index:] 
	print("Original:", myFile)
	print("Gefundene Endung:", suffix if suffix else "Keine")
	myFile = myFile.removesuffix(suffix)
	print(f"Ohne Endung: {myFile}")
else:
	print("Die Datei hat keine Endung")

