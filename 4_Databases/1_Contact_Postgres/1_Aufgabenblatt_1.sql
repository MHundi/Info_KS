/*markdown
## Aufgabenblatt 1
### Einfache SQL-Anfragen
*/

/*markdown
#### Aufgabe 1
Verbinden Sie sich mit dem Datenbank Server. Die Credentials dafür sind:
- host: 10.31.249.69
- Port: 5432
- database mondial
- user: students
- password: Inf20ormatik
- driver: postgres
*/

/*markdown
##### Aufgabe 2
Wie viele Zeilen hat die Relation `country`?
*/

/*markdown
#### Aufgabe 3
Geben Sie die Zahl der Länder an, die in der Realtion `country` eingetragen sind.
*/

select count(distinct(name)) from country



