negativ = False
szaznal_nagyobb = False

s = int(input("Hány számból álljon a számsorozat? "))

for i in range(s):
    n = int(input("Adj meg egy számot: "))

    if n > 100:
        szaznal_nagyobb = True
    if n < 0:
        negativ = True

    if szaznal_nagyobb or negativ:
        break

if negativ:
    print("Van negatív szám a sorozatban.")
else:
    print("Nincs negatív szám.")

if szaznal_nagyobb:
    print("Van 100-nál nagyobb szám.")
else:
    print("Nincs 100-nál nagyobb szám.")