# lees de lengte in
l = float(input("Geef je lengte (in m): "))
# lees de massa in
m = float(input("Geef je massa (in kg): "))

# bereken de BMI, maar toon deze nog niet
BMI = round(m / l**2, 1)

if BMI < 18.5:
    print(BMI, "ondergewicht")
elif 18.5 <= BMI < 25 :
    print(BMI, "gezond gewicht")
elif 25 <= BMI < 30 :
    print(BMI, "overgewicht")
else:
    print(BMI, "obesitas")
