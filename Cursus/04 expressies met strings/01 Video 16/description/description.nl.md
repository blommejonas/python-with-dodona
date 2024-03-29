In deze video leren we naast de 4 symbolen die toelaten om strings af te bakenen o.a. de lege string kennen. De backslash als speciaal teken met een bijzondere functie passeert ook de revue.

<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/81YEEXJAk8U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

## Dit weten we al
We gebruiken in Python witruimte zoals spaties om de leesbaarheid van onze code te vergroten. Dat betekent niet dat we zomaar overal spaties mogen noteren in onze code, maar een zekere vrijheid is er wel. Uiteraard moeten we rekening houden met de syntaxregels van Python. In stringwaarden bestaat er geen witruimte: elk teken telt er, dus ook elke patie.

## Gebruik van aanhalingstekens
<ul> 
  <li>Begin en einde van de string aanduiden met hetzelfde symbool.</li>
  <li>Mogelijkheden voor de symbolen:
    <ul>
      <li>enkele aanhalingsteken</li>
      <li>dubbele aanhalingsteken</li>
      <li>drievoudig enkele aanhalingsteken</li>
      <li>drievoudig dubbele aanhalingsteken</li>
    </ul>
    <div align="center">
      <img src="media/aanhalingstekens.png" align="center" width="275px" data-caption="Gebruik van aanhalingstekens." />
    </div>
    <br>
  </li>
  <li>Waarom verschillende mogelijkheden?<br>
    <p><b style="color:green;">Voorbeeld</b>:</p>
    <div align="center">
      <i>Harry Potter and the philosopher’s stone</i>
    </div>
    <br>
    <p>Voor deze string kan je geen enkelvoudig aanhalingsteken gebruiken omdat dit teken in de string zelf reeds voorkomt. Hier kan je dus opteren voor het dubbele         aanhalingsteken:</p>
    <div align="center">
      <img src="media/aanhalingstekens_vb1.png" align="center" width="350px" data-caption="Gebruik van aanhalingstekens - Voorbeeld 1." />
    </div>
    <br>
  </li>
  <li><p>Wanneer je gebruik maakt van drievoudige aanhalingtekens, worden deze door Python niet weergegeven.</p>
    <div align="center">
      <img src="media/aanhalingstekens_vb2.png" align="center" width="350px" data-caption="Gebruik van aanhalingstekens - Voorbeeld 2." />
    </div>
    <br>
    <p>Python kiest voor de enkelvoudige aanhalingstekens. Bij een enkelvoudig aanhalingsteken in de tekst plaatst Python een backslash. De backslash is GEEN                onderdeel van de string en heeft dus een bijzondere functie (zie later).</p>
  </li>
</ul>

## Getal als string of als getal opslaan
Kijk wat je met het getal wil doen. Indien je dit getal NIET gebruikt om berekeningen mee uit te voeren, kies je voor aanhalingstekens (en dus als string)!<br>
<p><b style="color:green;">Voorbeelden</b>:</p>
* telefoonnummer
* postnummer
* huisnummer
