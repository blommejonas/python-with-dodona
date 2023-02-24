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
    $$\frac{123}{5}=24.6$$<br>
    $$\frac{100}{6}=16.666...$$<br>
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
      <li><b style="color:green;">Algemeen</b>:<br>
        Om $$D$$ (het <b>deeltal</b>) te delen door $$d$$ (de <b>deler</b>), bepalen we de natuurlijke getallen $$q$$ (het <b>quotiënt</b>) en $$r$$ (de <b>rest</b>) zó dat<br><br>
        <div align="center">
          $$D = d \cdot q + r$$ en $$r < d$$
        </div>
      </li>
    </ul>
  </li>
</ul>
