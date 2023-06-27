a = input("Kirjuta siia üks tehe: ")


for märk in a:
    summa = 0
    
    tehe1 = a[1].split("+")
    if a[1] == "+":
        summa = int(a[0]) + int(a[2])
        
    tehe2 = a[1].split("-")
    if a[1] == "-":
        summa = int(a[0]) - int(a[2])
        
    tehe3 = a[1].split("*")    
    if a[1] == "*":
        summa = int(a[0]) * int(a[2])
        
    tehe4 = a[1].split("/")
    if a[1] == "/":
        summa = int(a[0]) / int(a[2])
        
        
        
print(summa)