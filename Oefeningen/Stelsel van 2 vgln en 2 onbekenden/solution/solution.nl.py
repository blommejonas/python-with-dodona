a = float(input("Vergelijking 1 - Geef de a-coëfficiënt in y=ax+b: "))
b = float(input("Vergelijking 1 - Geef de b-coëfficiënt in y=ax+b: "))
c = float(input("Vergelijking 2 - Geef de c-coëfficiënt in y=cx+d: "))
d = float(input("Vergelijking 2 - Geef de d-coëfficiënt in y=cx+d: "))

e = a-c
f = d-b

if e != 0:
     x = f/e
     y = a * x + b
     print("Unieke oplossing : (" +str(x)+ "," +str(y)+ ")")
else:
    if b==d:
        print("Er zijn oneindig veel oplossingen.")
    else:
        print("Dit stelsel is strijdig. Geen oplossingen.")
