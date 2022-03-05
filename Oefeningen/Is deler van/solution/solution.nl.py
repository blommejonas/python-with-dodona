D = int(input("Geef het deeltal : "))
d = int(input("Geef de deler : "))

q = D//d
r = D%d

if r==0 :
    print(d,"is een deler van",D)
    print("Het quotiënt is",q)
else :
    print(d,"is geen deler van",D)
    print("Het quotiënt is",q,"met rest",r)
