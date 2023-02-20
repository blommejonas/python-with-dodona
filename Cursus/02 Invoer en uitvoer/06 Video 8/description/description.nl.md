In deze video leren we de functie input() kennen, en leren we strings aan elkaar plakken.

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/BG4Ol_vLUB8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

## De functie input()
* Deze functie kan een vraag stellen en het antwoord afwachten.
* Tussen de haakjes: vraag die we willen stellen
* Na het intypen van het antwoord steeds ENTER drukken.
* Opmerking: de functie print() kan hier niet voor gebruikt worden. Deze kan wel een waarde (=stringwaarde) op het scherm tonen maar wacht vervolgens NIET op een antwoord.

<div align="center">
  <img src="media/input.png" align="center" width="250px" data-caption="De input()-functie." />
</div>

<div class="callout callout-info">
  <p>Het resultaat van de functie input() is automatisch een string-waarde, ook al heeft de gebruiker zelf geen aanhalingstekens geplaatst.</p>
</div>

* Het antwoord op de vraag is een waarde die we kunnen toekennen aan een variabele.

<div align="center">
  <img src="media/input_in_variabele.png" align="center" width="300px" data-caption="De input()-functie." />
</div>

## Het plakken van strings: concatenation
* We gebruiken hiervoor het ’+’-teken.
* In het voorbeeld worden 3 strings aan elkaar geplakt: voornaam, een spatie en familienaam.

<div align="center">
  <img src="media/concatenation.png" align="center" width="650px" data-caption="Het plakken van strings: concatenation." />
</div>

<b style="color:red">LET OP</b>: vergeet niet dat het resultaat van de functie input() een STRING-waarde is. Volgend programma geeft dus niet het gewenste resultaat:

<div align="center">
  <img src="media/concatenation_ongewenst.png" align="center" width="550px" data-caption="Het resultaat van de functie input() is een STRING-waarde." />
</div>

## Rol van het plusteken
Het plusteken gedraagt zich anders volgens datatype:
* stringwaarde + stringwaarde: ”12”+”34”wordt de string ’1234’
* integer + integer : 12 + 34 wordt de integer 46
