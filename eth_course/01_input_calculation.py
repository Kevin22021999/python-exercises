# Mein erstes Python-Programm
x = float(input("Geben Sie eine Zahl ein:\n"))
# Fordert den Benutzer auf, eine Zahl einzugeben, und speichert diese als Float in der Variable "x".
result = x * 2
# Multipliziert den Wert x mit 2 und speichert das Ergebnis in der Variable "result".
print("Eingabe:", x, "\nErgebnis:", result)
# Gibt das Produkt von x und 2 aus. Das \n sorgt für einen Zeiilenumbruch. Achtung \n muss in der String stehen, damit es funktioniert.
print(type(x))
# Gibt den Datentyp von x aus. Da x eine Benutzereingabe ist, wird es als Integer (int) interpretiert.