woord = input("Geef een woord: ")
omgekeerd = ""
palindroom = "Dit is geen palindroom."

for i in woord:
    omgekeerd = i + omgekeerd

if woord == omgekeerd:
    palindroom = "Dit is een palindroom."

print(woord,"-",omgekeerd)
print(palindroom)
