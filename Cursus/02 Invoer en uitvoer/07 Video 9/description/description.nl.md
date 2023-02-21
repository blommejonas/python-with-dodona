In deze video leren we de functie int() kennen, die ons toelaat een string om te zetten in een integer. Dit is de eerste uit een reeks “type conversion” functies.

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/OH2QwmtQO88" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

We weten ondertussen dat de waarde 12 verschilt van de waarde ”12”. De eerste waarde is een getal (een integer), de tweede waarde is een string. Integers en strings zijn verschillende datatypes. Dit verschil is belangrijk. Python gaat anders om met getallen dan met strings. Dat bleek o.a. bij de werking van het plusteken: een plusteken plakt strings aaneen, maar telt getallen op. 

## De functie int()
<ul>
  <li> int(waarde) controleert of de waarde een integer kan voorstellen. Indien dit zo is, geeft de functie die integer-waarde terug!
    <div align="center">
      <code>int(”15")</code> &#8594; 15
    </div>
  </li>
  <li> Deze functie zet dus een string om naar integer.</li>
  <li> Terug naar ons programma som van 2 getallen:
    <div align="center">
      <img src="media/functie_int.png" align="center" width="600px" data-caption="De functie int()." />
    </div>
    Een efficiëntere vorm van het programma is:
    <div align="center">
      <img src="media/functie_int_efficiënter.png" align="center" width="600px" data-caption="De functie int()." />
    </div>
  </li>
  <li> De functie int() kan je ook toepassen op een floatwaarde. Een float bestaat uit 2 delen: een geheel deel en een decimaal deel. De functie int() levert het         gehele deel op van de floatwaarde!
    <div align="center">
      <code>int(”15.23")</code> &#8594; 23
    </div>
  </li>
</ul>

