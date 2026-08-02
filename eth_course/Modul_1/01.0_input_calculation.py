"""
Kevin Schmutz
22.02.1999

"""

# Mein erstes Python-Programm
x = int(input("Geben Sie eine Zahl ein:\n"))
# Fordert den Benutzer auf, eine Zahl einzugeben, und speichert diese als Integer in der Variable "x".
result = x // 2
# Berechnet die Ganzzahlige Division von x durch 2 und speichert das Ergebnis in der Variable "result".
print("Eingabe:", x, "\nErgebnis:", result)
# Gibt das Ergebnis der Division von x durch 2 aus. Das \n sorgt für einen Zeilenumbruch. Achtung \n muss in der String stehen, damit es funktioniert.
print(type(x))
# Gibt den Datentyp von x aus. Da x eine Benutzereingabe ist, wird es als Integer (int) interpretiert.