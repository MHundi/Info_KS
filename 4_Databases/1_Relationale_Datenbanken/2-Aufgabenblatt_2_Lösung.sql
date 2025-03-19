Aufgaben und Lösungen

Länder mit bestimmten Anfangsbuchstaben:
Aufgabe: Schreiben Sie eine SQL-Abfrage, die alle Länder aus der Tabelle country anzeigt, deren Name mit dem Buchstaben „A“ beginnt.

SELECT name FROM country WHERE name LIKE 'A%';

Hauptstädte mit „burg“ im Namen:
Aufgabe: Finden Sie alle Hauptstädte (city.name), die in ihrem Namen die Zeichenfolge „burg“ enthalten. Nutzen Sie dabei einen Join mit der country-Tabelle.

SELECT city.name FROM city 
JOIN country ON city.id = country.capital 
WHERE city.name LIKE '%burg%';

Flüsse mit Endung „-er“:
Aufgabe: Ermitteln Sie alle Flüsse (river.name), deren Name auf „-er“ endet.

SELECT name FROM river WHERE name LIKE '%er';

Länder mit „land“ im Namen und deren Bevölkerung:
Aufgabe: Geben Sie alle Länder aus, die „land“ im Namen enthalten, zusammen mit ihrer Bevölkerung (population).

SELECT name, population FROM country WHERE name LIKE '%land%';

Seen mit genau 4 Buchstaben im Namen:
Aufgabe: Suchen Sie alle Seen (lake.name), deren Name genau vier Zeichen lang ist.

SELECT name FROM lake WHERE name LIKE '____';

Berge mit „Mount“ im Namen und deren Höhe:
Aufgabe: Finden Sie alle Berge (mountain.name), die „Mount“ im Namen enthalten, zusammen mit ihrer Höhe (elevation).

SELECT name, elevation FROM mountain WHERE name LIKE '%Mount%';

Städte mit „ville“ im Namen und deren Einwohnerzahl:
Aufgabe: Listen Sie alle Städte (city.name) auf, die „ville“ im Namen enthalten, und geben Sie die jeweilige Einwohnerzahl (population) aus.

SELECT name, population FROM city WHERE name LIKE '%ville%';

Hauptstädte mit „new“ im Namen und zugehöriges Land:
Aufgabe: Erstellen Sie eine Abfrage, die alle Hauptstädte mit „new“ im Namen und das zugehörige Land (country.name) anzeigt.

SELECT city.name, country.name FROM city 
JOIN country ON city.id = country.capital 
WHERE city.name LIKE '%new%';

Länder mit zwei aufeinanderfolgenden Vokalen im Namen:
Aufgabe: Finden Sie alle Länder (country.name), in deren Namen zwei aufeinanderfolgende Vokale (z. B. „aa“, „ee“, „oo“) vorkommen.

SELECT name FROM country WHERE name ~* '[aeiou]{2}';

Flüsse, die mit „A“ beginnen und durch mindestens zwei Länder fließen:
Aufgabe: Geben Sie alle Flüsse (river.name) aus, deren Name mit „A“ beginnt und die durch mindestens zwei verschiedene Länder fließen. Nutzen Sie hierfür einen Join mit der geography-Tabelle.

SELECT river.name FROM river 
JOIN geography ON river.id = geography.river 
GROUP BY river.name 
HAVING COUNT(DISTINCT geography.country) >= 2 
AND river.name LIKE 'A%';

