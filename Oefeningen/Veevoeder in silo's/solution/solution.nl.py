#input
b = float(input("Breedte van het veld (in meter)? "))
l = float(input("Lengte van het veld (in meter)? "))
c = float(input("Kubieke meter veevoeder per hectare? "))
z = float(input("Zijde grondvlak van de silo? "))
h = float(input("Hoogte van de silo? "))

#berekeningen
oppervlakte_veld = b*l/10000 #in hectare
veevoeder = oppervlakte_veld*c #in kubieke meter
inhoud_silo=z*z*h #in kubieke meter

volledig_gevulde_silos = int(veevoeder // inhoud_silo)
overig_veevoeder = veevoeder % inhoud_silo
hoogte_laatste_silo = overig_veevoeder / (z*z)

#output
print(volledig_gevulde_silos+1)
print(hoogte_laatste_silo)
