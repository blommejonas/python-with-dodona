Voor de aankoop van een woning lenen we een bedrag van $$V$$ euro aan een jaarlijkse rentevoet van $$r$$%. We lenen over een periode van $$N$$ jaar.

Van belang zijn volgende grootheden
* $$V$$ : het ontleende bedrag
* $$n$$ : het aantal perioden in maanden
* $$A$$ : het periodiek te betalen bedrag (= de aflossing + de rente)
* $$i$$ : de maandelijkse rente als fractie

Schrijf een programma die de volgende gegevens weergeeft:
* Het aantal perioden in maanden $$n$$.
* De maandelijkse rentevoet $$i * 100\%$$.
* Het maandelijks te betalen bedrag $$A$$ tot op 1 cent. Dit kan je berekenen als:

$$
A = \dfrac{i}{1-(1+i)^{-n}}*V
$$

* Het totaal terug te betalen bedrag $$V_{tot}$$ (het ontleende bedrag + de totale intresten).
* Het totaal bedrag aan intresten $$I_{tot}$$.

## Invoer
De waarden van $$V$$, $$r$$ en $$N$$, in die volgorde en elk op een afzonderlijke regel.

## Uitvoer
* 1e regel: n = $$n$$ maanden 
* 2e regel: maandelijkse rentevoet = $$i*100 \%$$ - af te ronden tot op 0.001 %
* 3e regel: maandelijks af te lossen bedrag = $$A$$ - af te ronden tot op 0.01 euro
* 4e regel: totaal terug te betalen bedrag = $$V_{tot}$$ euro
* 5e regel: totaal bedrag aan intresten = $$I_{tot}$$ euro

## Voorbeeld
Invoer:
```
260000
1.85
20
```
Uitvoer:
```
n = 240 maanden
maandelijkse rentevoet = 0.153 %
maandelijks af te lossen bedrag = 1295.01 euro
totaal terug te betalen bedrag = 310803.52 euro
totaal bedrag aan intresten = 50803.52 euro
```
