/*markdown
## Aufgabenblatt 1
*/

/*markdown
#### Aufgabe 1

Verbinden Sie sich mit dem Datenbank Server. Die Credentials dafür sind:

- host: 10.31.249.69
- Port: 5432
- database mondial
- driver: postgres
*/

/*markdown
##### Aufgabe 2

Wie viele Zeilen hat die Relation `country`

*/

select * from country

/*markdown
#### Aufgabe 3

Geben Sie die Zahl der Länder an, die in der Realtion `country` eingetragen sind.
*/

select count(distinct(name)) from country


/*markdown

*/