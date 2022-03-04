V = float(input("Het te ontlenen bedrag : "))
r = float(input("De jaarlijkse rentevoet : "))
N = float(input("Over hoeveel jaar loopt de lening : "))

n = N * 12
i = (1+r/100)**(1/12) - 1
A = (i*V)/(1-(1+i)**(-n))
totaal = A * n

print("n = " + str(int(n)) + " maanden")
print("i = " + str(round(i*100,3)) + " %")
print("A = " + str(round(A,2)) + " euro")
print("Totaal af te lossen bedrag = " + str(round(totaal,2)))
print("Totaal bedrag intresten    = " + str(round(totaal-V,2)))
