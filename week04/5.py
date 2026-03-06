szamok = [3, -1, 0, 8, -5, 7, 2, -9]

pozitiv = []
paros = []
paratlan = []

for szam in szamok:
    if szam > 0:
        pozitiv.append(szam)

        if szam % 2 == 0:
            paros.append(szam)
        else:
            paratlan.append(szam)

print("Pozitív számok:", pozitiv)
print("Páros számok:", paros)
print("Páratlan számok:", paratlan)