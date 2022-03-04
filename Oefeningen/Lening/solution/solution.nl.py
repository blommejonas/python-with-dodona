V = float(input("Het te ontlenen bedrag : "))
r = float(input("De jaarlijkse rentevoet (in %) : "))
n = int(input("Over hoeveel maanden loopt de lening : "))

i = (1+r/100)**(1/12) - 1
A = (i*V)/(1-(1+i)**(-n))
totaal = A * n

print("i = " + str(round(i*100,4)) + " %")
print("A = " + str(round(A,2)) + " euro")
print("V_tot = " + str(round(totaal,2)) + " euro")
