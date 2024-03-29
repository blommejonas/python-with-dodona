# Het datatype float
Floats, wat kort is voor “floating-point getallen” of “gebroken getallen”, zijn **getallen met decimalen**. Bijvoorbeeld: <code>3.14159265</code> is een float. Merk op dat je een punt in plaats van een komma moet gebruiken als decimaal-scheider. Veel landen (inclusief België en Nederland) gebruiken een komma als decimaal-scheider, maar Python houdt zich aan de conventie van Engelstalige landen en gebruikt daarom de punt.

## Wanneer gebruikt Python een float?
Als je een getal met een punt ingeeft, interpreteert Python dat automatisch als een float.

Daarnaast heb je in videoles 10 over datatypes ook geleerd dat de deling van twee integers automatisch een float als resultaat geeft in Python, zelfs als de deling rest 0 heeft.

<img src="media/afronden_bij_float.png" align="center" width="200px" data-caption="10/2 geeft als resultaat de float 5.0" />

## Een float omzetten naar een integer met de functie int()
<p>Het is niet altijd handig dat Python de deling van twee integers automatisch als float labelt. We kunnen daarom het resultaat opnieuw omzetten naar een integer met de functie <code>int()</code>.</p>
<img src="media/afronden_bij_float_toInt.png" align="center" width="200px" data-caption="10/2 geeft als resultaat de float 5.0" />

<p>Let wel op: als je getal niet geheel is, gaat de functie <code>int()</code> in feite alles na de komma weglaten, zowel bij positieve als bij negatieve getallen.</p>
<img src="media/afronden_bij_float_toInt_opletten.png" align="center" width="200px" data-caption="Afronden met behulp van het int()-commando." />

<p>Merk op dat er hierboven iets geks gebeurt voor <code>5.9999999999999999</code>. Dat is omdat we voorbij de precisie gaan waarmee Python werkt voor floats.</p>


## Precisie van floats in Python
Er zijn bepaalde begrenzingen aan de grootte van de floats en aan de precisie. Het is onwaarschijnlijk dat je ooit de maximale groottes bereikt, aangezien Python wetenschappelijke notatie voor grote getallen gebruikt. **Maar door de manier waarop Python floats opslaat, kunnen bepaalde getallen niet precies vastgelegd worden. Dit zorgt soms wel voor problemen.**

Bijvoorbeeld: het statement <code>print((431/100)*100)</code> geeft als antwoord <code>430.99999999999994</code>, en niet 431 zoals je zou verwachten. Als je weet dat de uitkomst van een berekening waarin floats zitten een integer moet zijn, dan doe je er goed aan om de uitkomst af te ronden naar het dichtstbijzijnde gehele getal. Dat kun je doen met behulp van de <code>round()</code> functie.

<img src="media/afronden_bij_float_precisie.png" align="center" width="200px" data-caption="Precisie bij werken met floats." />

# De functie round()
## Een float omzetten naar een integer met de functie round()
Zoals je hieronder ziet, gaat de functie <code>round()</code> een getal afronden naar de dichtsbijzijnde integer.

<img src="media/functie_round1.png" align="center" width="200px" data-caption="De functie round()." />

**Maar opgelet: de functie <code>round()</code> in Python volgt helaas niet altijd de afspraken die we binnen de wiskunde hebben over afronden.** In het bijzonder wanneer het eerste cijfer dat we weglaten een 5 is, wijken de regels van Python af van de wiskundige regels. Wij zouden bijvoorbeeld 1,5 afronden naar 2 en 2,5 afronden naar 3. Zoals je hieronder ziet, doet Python iets anders:

<img src="media/functie_round2.png" align="center" width="200px" data-caption="De functie round()." />

In dit geval kiest Python ervoor om af te ronden naar het dichtsbijzijnde even getal. Dit is slechts een detail, maar we vermelden het toch voor de volledigheid.

## Afronden tot op een aantal cijfers na de komma met de functie round()
Je kan met de functie <code>round()</code> een getal ook afronden tot een gegeven aantal cijfers na de komma.

<img src="media/functie_round_na_komma.png" align="center" width="200px" data-caption="De functie round(): afronden tot een gegeven aantal cijfers na de komma." />

Merk op: ook hier volgt Python z’n eigen regels als het eerste cijfer dat wordt weggelaten een 5 is.
