x = int(input("Geef de totale oppervlakte van de kamer : "))

#Aantal grote verfpotten
agv = (x*2)//40

#Aantal kleine verfpotten
akv = (((x+2)%40) // 10) + 1

print(agv, akv)
print(agv * 110 + akv * 35)
