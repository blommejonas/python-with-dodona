In deze video maken we kennis met het <code>if</code>-statement, in z’n meest éénvoudige vorm. We zien de analogie tussen de taalkundige constructie ALS/DAN en het <code>if</code>-statement.

* We leren de syntax-regels die gevolgd moeten worden om een <code>if</code>-statement toe te passen in Python, kennen.
* We zien het nut in van het inspringen van code (indentation), waardoor er zogenaamde “code blocks” worden gevormd.
* We werken een voorbeeld van een <code>if</code>-statement uit in de editor.

<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/ykh3f7f9lFE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

## Het if-statement
<p>Een <b>statement</b> is een stukje programmacode dat een - door de computer uit te voeren - taak beschrijft.</p>
<p>Het <b><code>if</code>-statement</b> (in zijn eenvoudigste vorm) beschrijft welke taken moeten uitgevoerd worden wanneer een specifieke booleaanse expressie evalueert naar de waarde True</p>

## Komt overeen met ALS/DAN
<b>ALS</b> <i>booleaanse expressie</i> <b>DAN</b><br>
&nbsp;&nbsp;&nbsp; <i>taak 1</i> <br>
&nbsp;&nbsp;&nbsp; <i>taak 2</i> <br>
&nbsp;&nbsp;&nbsp; <i>taak 3</i> <br>

## Van ALS/DAN constructie naar if-statement
<ul>
  <li> Syntax-regels voor if-statement: <br>
    &nbsp;&nbsp;&nbsp;&nbsp; ALS → if <br>
    &nbsp;&nbsp;&nbsp;&nbsp; DAN → : <br>
    &nbsp;&nbsp;&nbsp;&nbsp; tussen ALS en DAN → booleaanse expressie <br>
    &nbsp;&nbsp;&nbsp;&nbsp; na de dubbelpunt → inspringende codeblok met uit te voeren taken <br>
    &nbsp;&nbsp;&nbsp;&nbsp; inspringen van code: 4 spaties <br>
  </li>
  <li> Samengevat:
    <pre><code><b>if</b> <i>booleaanse expressie</i> :
    <i>taak 1</i>
    <i>taak 2</i>
    <i>taak 3</i> </code></pre>
  </li>
</ul>

De booleaanse expressie is een voorwaarde vandaar dat het <code>if</code>-statement ook conditional statement genoemd wordt.

## Code block
* start wanneer code inspringt (inspringen → indentation)
* eindigt met de terugkeer naar het eerdere niveau
* alle tussenliggende regels maken deel uit van hetzelfde blokje programmacode, van dezelfde "code block"
* "code blocks" kunnen deel uitmaken van grotere "code blocks"
* wordt er begonnen aan de uitvoering van een "code block", dan wordt de "code block", in principe, volledig doorlopen door Python.

## Keyword
Het woord <b>if</b> is een Python keyword.
