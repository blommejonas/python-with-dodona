Schrijf een programma dat achtereenvolgens de lengte $$l$$ (in m) en de massa $$m$$ (in kg) van de gebruiker vraagt. Het berekent de BMI van de gebruiker, rondt deze af op 1 cijfer na de komma en interpreteert vervolgens deze afgeronde waarde aan de hand van de tabel.

<div class="dodona-centered-group">
  <table class="table" style="width:50%">
    <thead>
      <tr>
        <th>BMI</th>
        <th>interpretatie</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>BMI $$<$$ 18.5</td>
        <td>ondergewicht</td>
      </tr>
      <tr>
        <td>18.5 $$\leq$$ BMI $$<$$ 25</td>
        <td>gezond gewicht</td>
      </tr>
      <tr>
        <td>25 $$\leq$$ BMI $$<$$ 30</td>
        <td>overgewicht</td>
      </tr>
      <tr>
        <td>BMI $$\geq$$ 30</td>
        <td>obesitas</td>
      </tr>
    </tbody>
  </table>
</div>

## Invoer
Eerst wordt gevraagd naar de lengte $$l$$ (in m) van de persoon. Vervolgens wordt gevraagd naar diens massa $$m$$ (in kg).

## Uitvoer
Het programma toont op één lijn de BMI (afgerond op 1 cijfer na de komma) en de interpretatie.

## Voorbeeld 1
Invoer:
```
1.68
65
```
Uitvoer:
```
23.0 gezond gewicht
```

## Voorbeeld 2
Invoer:
```
1.95
69.5
```
Uitvoer:
```
18.3 ondergewicht
```
