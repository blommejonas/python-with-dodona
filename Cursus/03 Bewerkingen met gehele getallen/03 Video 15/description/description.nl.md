In deze video leren we de dubbele breukstreep kennen als het symbool voor de geheeltallige deling of floor division, en het percentageteken als symbool voor de modulo- of restberekening.<br>

Dit lijkt misschien ingewikkeld, maar eigenlijk is dit de deling die je in de lagere school hebt geleerd. Bijvoorbeeld: 11 gedeeld door 2 is 5 met rest 1.

<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/wf8hx2QRitg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

## Euclidische deling van natuurlijke getallen
Er bestaat <b>2 soorten delingen</b>:
<ul>
  <li>een gewone deling, ook wel een <b>deling met komma</b> genoemd<br>
    <b style="color:green;">Voorbeelden</b>:<br>
    $$\frac{123}{5}=24,6$$<br>
    $$\frac{100}{6}=16,666...$$<br>
    In Python gebruiken we hiervoor de slash (/).
  </li><br>
  <li>een deling met rest, ook een <b>euclidische deling</b> genoemd<br>
    <ul>
      <li><b style="color:green;">Voorbeeld</b>:<br>
        Bij de euclidische deling van 33 door 4 is 8 het quotiënt en 1 de rest. Hierbij geldt:<br><br>
        <div align="center">
          $$33 = 4 \cdot 8 + 1$$ en $$1 < 4$$
        </div>
        <br>
        Hierbij is 33 het deeltal, 4 de deler, 8 het quotiënt en 1 de rest.<br>
        De rest is steeds strikt kleiner dan de deler.
      </li>
      <br>
      <li><b style="color:green;">Algemeen</b>:<br>
        Om $$D$$ (het <b>deeltal</b>) te delen door $$d$$ (de <b>deler</b>), bepalen we de natuurlijke getallen $$q$$ (het <b>quotiënt</b>) en $$r$$ (de <b>rest</b>) zó dat<br><br>
        <div align="center">
          $$D = d \cdot q + r$$ en $$r < d$$
        </div>
      </li>
      <br>
      In deze les bestuderen we hoe we de geheeltallige deling met quotiënt en rest kunnen uitvoeren in Python.
    </ul>
  </li>
</ul>

## Syntax
<ul>
  <li><b>Floor division</b> of <b>geheeltallige deling</b> : // <br><br>
    <div align="center">
      $$D$$ // $$d$$ = $$q$$
    </div>
    <br>
    De floor division of geheeltallig deling (//) levert ons dus het <b>quotiënt</b> bij deling van $$D$$ door $$d$$.
  </li>
  <li><b>Modulo</b> of <b>restberekening</b>: %
    <div align="center">
      $$D$$ % $$d$$ = $$r$$
    </div>
    <br>
    De modulo of restberekening (%) levert ons dus de <b>rest</b> bij deling van $$D$$ door $$d$$.
  </li>
</ul>

## Voorbeeld
Splits een groep van 317 mensen in groepjes van 23.
<ul>
  <li><b style="color:blue;">Gegeven:</b>
    <ul>
      <li>Totaal: 317</li>
      <li>Groepsgrootte: 23</li>
    </ul>
  </li>
  <li>We stellen ons de volgende vragen:
    <ul>
      <li>Hoeveel volledige groepen kunnen we vormen?</li>
      <li>Hoeveel mensen blijven er over?</li>
    </ul>
  </li>
  <li><b style="color:blue;">Oplossing:</b>
    <ul>
      <li><b>Hoeveel volledige groepen kunnen we vormen?</b><br>
        We berekenen: 317/23 = 13,7826.<br>
        De oplossing is het getal voor de komma, dus 13.<br>
        Hiervoor kunnen we de floor division gebruiken:<br>
        <div align = "center">
          317 // 23 = 13
        </div>
        <br>
      </li>
      <li><b>Hoeveel mensen blijven er over?</b><br>
        We berekenen hiervoor 317 − 13 · 23 = 18.<br>
        We kunnen de rest bij deling van 317 door 23 in 1 stap vinden m.b.v. de bewerking modulo:<br>
        <div align = "center">
          317 % 23 = 18
        </div>
      </li>
    </ul>
  </li>
</ul>
