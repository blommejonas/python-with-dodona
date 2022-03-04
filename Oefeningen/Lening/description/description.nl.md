Voor de aankoop van een woning lenen we een bedrag van $$V$$ euro aan een jaarlijkse rentevoet van $$r$$%. We lenen over een periode van $$n$$ maanden.

Schrijf een programma die de volgende gegevens weergeeft:
* De maandelijkse rentevoet $$i$$ in %.
* Het maandelijks te betalen bedrag $$A$$ tot op 1 cent. Dit kan je berekenen als:

$$
A = \dfrac{\dfrac{i}{100}}{1-\left(1+\dfrac{i}{100}\right)^{-n}}*V
$$

* Het totaal terug te betalen bedrag $$V_{tot}$$ (het ontleende bedrag + de totale intresten).

## Invoer
De waarden van $$V$$, $$r$$ en $$n$$, in die volgorde en elk op een afzonderlijke regel.

## Uitvoer
Geef weer in het tekstformaat zoals weergegeven in de voorbeelden.
* 1e regel: maandelijkse rentevoet $$i$$ (af te ronden tot op 0.0001 %)
* 2e regel: maandelijks af te lossen bedrag $$A$$ (af te ronden tot op 0.01 euro)
* 3e regel: totaal terug te betalen bedrag $$V_{tot}$$ euro

## Voorbeeld 1
Invoer:
```
260000
1.85
240
```
Uitvoer:
```
i = 0.1529 %
A = 1295.01 euro
V_tot = 310803.52 euro
```

## Voorbeeld 2
Invoer:
```
120000
0.862
180
```
Uitvoer:
```
i = 0.0716 %
A = 710.76 euro
V_tot = 127936.21 euro
```
