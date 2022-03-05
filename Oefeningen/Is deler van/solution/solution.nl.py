D = int(input("Geef het deeltal : "))
d = int(input("Geef de deler : "))

q = D//d
r = D%d

if r==0 :
    print(d,"is een deler van",str(D)+".")
    print("Het quotiënt is",str(q)+".")
else :
    print(d,"is geen deler van",str(D)+".")
    print("Het quotiënt is",q,"met rest",str(r)+".")
