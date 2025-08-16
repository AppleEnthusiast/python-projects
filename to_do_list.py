
print("Willkommen zu deiner To-Do-Liste!")
todo_list = []  # Leere Liste für Aufgaben

while True:
    print("\nWas möchtest du tun?")
    print("1 - Aufgabe hinzufügen")
    print("2 - Aufgaben anzeigen")
    print("3 - Aufgabe erledigen")
    print("4 - Programm beenden")

    choice = input("Wähle eine Option: ")

    if choice == "1":
        aufgabe = input("Welche Aufgabe soll hinzugefügt werden? ")
        todo_list.append(aufgabe)
        print(f"'{aufgabe}' wurde hinzugefügt.")

    elif choice == "2":
        if len(todo_list) == 0:
            print("Keine Aufgaben vorhanden.")
        else:
            print("Deine Aufgaben:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("Keine Aufgaben zum Erledigen.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            num = int(input("Welche Aufgabe ist erledigt? (Nummer eingeben): "))
            if 1 <= num <= len(todo_list):
                erledigt = todo_list.pop(num - 1)
                print(f"'{erledigt}' wurde entfernt.")
            else:
                print("Ungültige Nummer.")

    elif choice == "4":
        print("Programm beendet. Bis bald!")
        break

    else:
        print("Ungültige Eingabe, bitte erneut versuchen.")

