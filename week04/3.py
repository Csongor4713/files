maxi=0
index=0
n=int(input("Add meg hány darab számot szeretnél megadni:"))
for i in range(0,n):
    x=int(input("Adj meg egy szamot:"))
    if x>maxi:
        maxi=x
        index=i
print("Az általad megadott számok közül a legnagyobb: ",maxi)
print("Az általad megadott legnagyobb számnak az indexe: ",index)