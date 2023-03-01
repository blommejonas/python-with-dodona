a = int(input("Geef de coëfficiënt a in f(x)=ax²+bx+c : "))
b = int(input("Geef de coëfficiënt b in f(x)=ax²+bx+c : "))
c = int(input("Geef de coëfficiënt c in f(x)=ax²+bx+c : "))

x_T = int(-b/(2*a))
y_T = int(a*x_T**2 + b*x_T + c)

print("Top parabool: ("+str(x_T)+ ", " +str(y_T)+ ")")
print("Vergelijking S.A.: x = " +str(x_T))
