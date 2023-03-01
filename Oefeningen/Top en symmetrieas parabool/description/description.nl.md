Schrijf een programma dat vraagt naar de coëfficiënten van de tweedegraadsfunctie $$f(x) = ax^2 + bx + c$$ met $$a \in \mathbb{R}_0$$.

Vervolgens bepaalt het programma:
1. de coördinaat van de top <br>
   $$x_T = \alpha = -\dfrac{b}{2a}$$ <br>
   $$y_T = \beta  = f(\alpha)$$
2. de vergelijking van de symmertrie-as: $$x = \alpha$$
   
## Invoer
- Eerst wordt gevraagd naar de waarde van $$a$$.
- Vervolgens wordt gevraagd naar de waarde van $$b$$.
- Tenslotte wordt gevraagd naar de waarde van $$c$$.
Alle waarden worden ingegeven als natuurlijke getallen en $$a$$ mag niet nul zijn.

## Uitvoer
- Op de eerste regel verschijnt de coördinaat van de top van de parabool: "Top parabool: $$(x_T, y_T)$$"
- Op de tweede regel verschijnt de vergelijking van de symmetrieas van de parabool: "Vergelijking S.A.: $$x = x_T$$"
We bekijken enkel de gevallen waarbij de x- en y-coördinaat natuurlijke getallen zijn.

## Voorbeeld 1
Invoer:
```
3
12
-15
```
Uitvoer:
```
Top parabool: (-2, -27)
Vergelijking S.A.: x = -2
```

## Voorbeeld 2
Invoer:
```
-2
4
-5
```
Uitvoer:
```
Top parabool: (1, -3)
Vergelijking S.A.: x = 1
```
