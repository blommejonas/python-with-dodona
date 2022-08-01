# Vraag om de parameters van de rechten
# r <-> ax+by+c=0
# r <-> ux+vu+w=0
a = float(input("Vergelijking r - Geef de a-coëfficiënt in ax+by+c=0: "))
b = float(input("Vergelijking r - Geef de b-coëfficiënt in ax+by+c=0: "))
c = float(input("Vergelijking r - Geef de c-coëfficiënt in ax+by+c=0: "))
u = float(input("Vergelijking s - Geef de u-coëfficiënt in ux+vy+w=0: "))
v = float(input("Vergelijking s - Geef de v-coëfficiënt in ux+vy+w=0: "))
w = float(input("Vergelijking s - Geef de w-coëfficiënt in ux+vy+w=0: "))

# Rewrite to the form r <-> y=p1x+q1 and s <-> y=p2x+q2
p1 = -a / b
q1 = -c / b
p2 = -u / v
q2 = -w / v

e = p1 - p2
f = q2 - q1

if e != 0:
    x = f / e
    y = p1 * x + q1
    print("De rechten zijn snijdend.")
    print("Het snijpunt heeft als coördinaat (" + str(x) + "," + str(y) + ")")
else:
    if q1 == q2:
        print("De rechten zijn samenvallend.")
        print("De rechten hebben oneindig veel punten gemeenschappelijk.")
    else:
        print("De rechten zijn strikt evenwijdig.")
        print("De rechten hebben geen enkel punt gemeenschappelijk.")
