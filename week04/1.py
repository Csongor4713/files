x=int(input("Adj meg n darab számot:"))
s=0
s_pos=0
for i in range(0,x):
    n=int(input("Adj meg egy számot: "))
    s+=n
    if(n>0):
        s_pos+=n
print("A beolvasott számok összege: ",s)
print("A pozitív beolvasott számok összege:" ,s_pos)