eredmenyek = [45, 78, 90, 32, 67, 50, 98, 44]

atlag = sum(eredmenyek) / len(eredmenyek)

sikeres = 0
for pont in eredmenyek:
    if pont >= 50:
        sikeres += 1

legjobb = max(eredmenyek)

elegtelen = False
for pont in eredmenyek:
    if pont < 50:
        elegtelen = True

print("Átlag:", atlag)
print("Sikeres vizsgák száma:", sikeres)
print("Legjobb eredmény:", legjobb)
print("Van-e elégtelen:", elegtelen)