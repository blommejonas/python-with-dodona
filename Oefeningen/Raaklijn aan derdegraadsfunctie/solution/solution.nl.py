#Coëfficiënten van de derdegraadsveelterm
a3 = float(input("Wat is de coëfficiënt bij x³? "))
a2 = float(input("Wat is de coëfficiënt bij x²? "))
a1 = float(input("Wat is de coëfficiënt bij x? "))
a0 = float(input("Wat is de constante term? "))

#Bepaal de coëfficiënten van de afgeleide functie
b2 = a3 * 3
b1 = a2 * 2
b0 = a1

#Vraag in welk punt de raak aan de functie bepaald moet worden
x = float(input("In welke waarde van x moet de raaklijn bepaald worden? "))

#Bereken het beeld van x
f_x = a3 * x**3 + a2 * x**2 + a1 * x + a0

#Bereken de richtingscoëfficiënt van de raaklijn
rico_t = b2 * x**2 + b1 * x + b0
#Bereken de b-waarde in y = ax + b met (x,y) = (x,f_x)
b = f_x - rico_t * x

if rico_t==0:
    print("De vergelijking van de raaklijn aan f in P(" +str(x)+ ", " +str(round(f_x,2))+ ") is y = " +str(round(b,1))+".")
else:
    if b>0:
        print("De vergelijking van de raaklijn aan f in P(" +str(x)+ ", " +str(round(f_x,2))+ ") is y = " +str(round(rico_t,1))+ "x + " + str(round(b,1))+".")
    elif b<0:
        print("De vergelijking van de raaklijn aan f in P(" +str(x)+ ", " +str(round(f_x,2))+ ") is y = " +str(round(rico_t,1))+ "x - " + str(abs(round(b,1)))+".")
    else:
        print("De vergelijking van de raaklijn aan f in P(" +str(x)+ ", " +str(round(f_x,2))+ ") is y = " +str(round(rico_t,1))+ "x"+".")
