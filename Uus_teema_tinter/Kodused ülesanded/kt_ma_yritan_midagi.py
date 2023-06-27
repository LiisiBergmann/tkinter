a = input("Sisesta siia üks tehe: ")

def aritmeetikatehe():
    summa = 0
    for arv in a:
        if a == "+":
            tehe = a[0].split("\\+")
            summa = tehe[0]
            for b in tehe:
                summa += summa
                print(summa)
        if a == "-":
            tehe1 = a.split("\\-")
            tehe1 = tehe1[0]
            for b in tehe1:
                summa -= summa
                print(summa)

        if a == "*":
            tehe2 = a.split("\\*")
            tehe2 = tehe2[0]
            for c in tehe2:
                summa *= summa
                print(summa)

        if a == "/":
            tehe3 = a.split("\\/")
            tehe3 = tehe3[0]
            for c in tehe3:
                summa *= summa
                print(summa)



        return aritmeetikatehe(summa)