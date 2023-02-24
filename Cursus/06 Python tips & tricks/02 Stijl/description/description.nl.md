## Spaties
Misschien is het je opgevallen dat er in de voorbeelden veel spaties gebruikt worden. De meeste van deze zaken zijn gewoon **persoonlijke stijl**. De spaties bij de haakjes en rond de operatoren zijn niet nodig. Python begrijpt de code ook prima als ze er niet staan. De volgende vier regels code zijn equivalent:

<pre><code># Equivalente regels code
print( 2 + 3 )
print(2+3)
print( 2+3)
print ( 2 + 3 )
</code></pre>

Het “vastplakken” van het openingshaakje aan de functienaam doet vrijwel iedere programmeur, maar voor de rest verschillen de stijlen van spaties plaatsen tussen programmeurs. Je kunt hierin je eigen stijlvoorkeur gebruiken, je hoeft niet de voorgestelde stijl te volgen. Maar ik raad je wel aan om een consistente stijl te gebruiken, want dat maakt je code leesbaarder, zelfs voor programmeurs die er een andere stijl op nahouden.

Merk op dat de code hierboven een **hekje #** (Engels: “hash mark”) heeft op de eerste regel, waarna een tekst volgt die wat details over de code uitlegt. Deze regel is een commentaarregel: als je een # gebruikt in je code (behalve als die in een string staat, natuurlijk) dan is alles wat rechts van de # staat op de regel commentaar, dat door Python genegeerd wordt. Je kunt commentaar gebruiken om details over je code te geven, als je denkt dat uitleg nodig is.

## Namen van variabelen
### Namen van variabelen: regels
We herhalen de regels voor het geven van namen aan variabelen uit videoles 7.

Je bent vrij om namen te kiezen voor variabelen, als je je daarbij maar aan een aantal eenvoudige regels houdt:

Een naam van een variabele mag slechts bestaan uit letters, cijfers, en “underscores” (_)
Een naam van een variabele moet beginnen met een letter of een underscore.
Een naam van een variabele mag geen gereserveerd woord zijn. “Gereserveerde woorden” (of “keywords”) zijn:

<pre><code>False       class       finally     is          return
None        continue    for         lambda      try
True        def         from        nonlocal    while
and         del         global      not         with
as          elif        if          or          yield
assert      else        import      pass
break       except      in          raise
</pre></code>

Je mag zowel hoofd- als kleine letters gebruiken in namen van variabelen, maar je moet wel beseffen dat Python “case sensitive” is, dus gevoelig voor de verschillen tussen hoofd- en kleine letters. Bijvoorbeeld, de variabele naam <code>wereld</code> is voor Python niet hetzelfde als de variabele naam <code>Wereld</code>.

### Namen van variabelen: conventies
Programmeurs houden zich aan een flink aantal conventies wanneer ze variabele namen kiezen. De belangrijkste zijn de volgende:

* Programmeurs kiezen nooit een variabele naam die ook de naam is van een functie (of het nu een standaard Python functie betreft of een functie die ze zelf hebben geschreven). Als je dat doet, loop je de kans dat de functie niet langer door de code gebruikt kan worden, wat kan leiden tot uitermate vreemde fouten.
* Programmeurs proberen variabele namen zo te kiezen dat ze betekenisvol zijn in de context van het programma. Bijvoorbeeld, een variabele die het aantal seconden in een week bijhoudt, zou de naam secs_per_week kunnen hebben, maar niet ik_haat_mijn_baan. Het zou nog erger zijn om het aantal seconden in een week op te slaan in een variabele secs_per_maand.
* Een uitzondering op het kiezen van betekenisvolle variabele namen is het kiezen van namen voor “wegwerp variabelen,” dat wil zeggen, variabelen die slechts in een klein deel van de code gebruikt worden, naderhand niet meer gebruikt worden, en die van zichzelf eigenlijk geen betekenis hebben. Programmeurs kiezen vaak éénletter namen voor dit soort variabelen, zoals i of j.
* Om verwarring tussen hoofd- en kleine letters te vermijden, gebruiken programmeurs meestal alleen kleine letters in variabele namen.
* Als een variabele naam uit meerdere woorden bestaat, zetten programmeurs underscores tussen die woorden.
* Programmeurs kiezen nooit variabele namen die beginnen met een underscore. Het gebruik van dat soort namen is voorbehouden aan de auteurs van Python.
Je moet proberen je voor je eigen code ook aan deze conventies te houden. De conventie met betrekking tot het kiezen van betekenisvolle variabele namen is vooral belangrijk, omdat het code leesbaar en onderhoudbaar maakt. Kijk bijvoorbeeld eens naar de volgende code:

<pre><code>a = 3.14159265
b = 7.5
c = 8.25
d = a * b * b * c / 3
print( d )
</code></pre>
Snap je wat deze code doet? Je ziet waarschijnlijk wel dat er een benadering van π in voorkomt, maar wat stelt d voor?

Deze code berekent het volume van een kegel. Dat zou je waarschijnlijk niet geraden hebben, maar dat is wel wat er gebeurt. Nu vraag ik je de code zo te wijzigen dat het volume van een kegel met een hoogte van 4 meter berekend wordt. Welke wijziging maak je in de code?A Als de hoogte in de formule staat, is het waarschijnlijk b of c. Maar welk van de twee? Als je een beetje wiskunde kent, en je bekijkt de berekening van d, dan zie je dat b gekwadrateerd wordt in de berekening. Dat lijkt dus de voet van de kegel te zijn, wat zou betekenen dat c de hoogte is. Maar dat kun je niet zeker weten.

Bekijk nu de volgende, equivalente code:

<pre><code>pi = 3.14159265
straal = 7.5
hoogte = 8.25
volume_van_kegel = pi * straal * straal * hoogte / 3
print( volume_van_kegel )
</code></pre>

Dat is een stuk leesbaarder, nietwaar? Als ik je nu vraag de code te wijzigen, verwacht ik niet dat je ook maar een moment zult twijfelen.

Code met betekenisvolle namen wordt vaak “zelf-documenterend” genoemd; je hoeft er geen commentaarregels in op te nemen om de gebruiker te laten begrijpen wat de code doet en hoe het werkt. Dat neemt niet weg dat in bovenstaande code een commentaarregel als:

<pre><code># berekening van volume van kegel met straal 7.5 en hoogte 8.25</code></pre>

niet zou misstaan.

### Constanten
Veel programmeertalen geven je de mogelijkheid om “constanten” te creëren, wat waardes zijn die aan een variabele zijn toegekend, die geen andere waarde meer kan krijgen. Het is conventie dat alle letters in dit soort variabele namen hoofdletters zijn. Constanten kunnen gebruikt worden om code leesbaarder en onderhoudbaarder te maken. Bijvoorbeeld, om voor een rekening van €24,95 exclusief BTW het eindbedrag te berekenen, kun je de volgende code gebruiken:

<pre><code>
totaal = 24.95
eind_totaal = int(100 * totaal * 1.21)/100
print(eind_totaal)
</code></pre>

Het is echter leesbaarder om te schrijven:

<pre><code>BTW_FACTOR = 1.21
CENTEN = 100
totaal = 24.95
eind_totaal = int( CENTEN * totaal * BTW_FACTOR ) / CENTEN
print( eind_totaal )
</code></pre>

Niet alleen is dit leesbaarder, het maakt het ook gemakkelijk om de code aan te passen als de BTW tarieven wijzigen. Zeker als constanten meerdere malen terugkeren in code, is het beter om ze eenmalig een waarde te geven bovenin de code, waar ze gemakkelijk gevonden en gewijzigd kunnen worden. Als het numerieke waarden betreft, zoals de BTW factor, spreekt men vaak over “magische getallen”: getallen waarvan de waarde voor de code een speciale betekenis heeft, die niet duidelijk is als je alleen het getal ziet. Je bent dus beter af als je een betekenisvolle naam ziet in plaats van een getal.

Hoewel constanten erg nuttig kunnen zijn, worden ze niet door Python ondersteund (wat erg jammer is). Dat wil zeggen dat in de code hierboven BTW_FACTOR een reguliere variabele is die overal in de code gewijzigd kan worden. Het is echter de gewoonte om dit soort variabelen die volledig uit hoofdletters bestaan te beschouwen als constanten die niet in de code gewijzigd mogen worden nadat ze hun initiële waarde hebben gekregen. Ik raad je aan dit soort semi-constanten te gebruiken als er magische getallen in je code voorkomen.
