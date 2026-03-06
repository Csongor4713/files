paros_db=0
negativ_db=0
n=int(input("Adj meg egy számot, 0-ra kilép:"))

while n!=0:
    if n%2==0:
        paros_db+=1
    if n<0:
        negativ_db+=1
    n=int(input("Adj meg egy számot, 0-ra kilép:"))
print("A páros számok darabjainak összege:",paros_db)
print("A negatív számok darabjainak összege:",negativ_db)