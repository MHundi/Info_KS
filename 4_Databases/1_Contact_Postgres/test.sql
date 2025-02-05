/*markdown
# Arbeitsblatt 1: Einfache SQL-Abfragen

**Thema:** Einführung in SQL-Abfragen

**Ziel:** Die Schüler sollen grundlegende SQL-Befehle anwenden können, um Daten aus der Mondial-Datenbank abzufragen.

## Teil 1: Grundlegende SQL-Befehle

1. **SELECT und FROM**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die alle Informationen aus der Tabelle `country` abruft.
   
     ```sql
     SELECT * FROM country;
     ```

2. **WHERE**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die alle Informationen über Länder abruft, deren Bevölkerung größer als 50 Millionen ist.
   
     ```sql
     SELECT * FROM country WHERE population > 50000000;
     ```

3. **ORDER BY**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die alle Länder nach ihrer Bevölkerungsgröße in absteigender Reihenfolge sortiert.
   
     ```sql
     SELECT * FROM country ORDER BY population DESC;
     ```

## Teil 2: Praktische Übungen

4. **Übung 1: Abfrage nach Kontinent**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die den Namen und die Bevölkerung aller Länder in Europa abruft.
   
     ```sql
     SELECT name, population FROM country WHERE continent = 'Europe';
     ```

5. **Übung 2: Abfrage nach Hauptstadt**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die den Namen und die Hauptstadt aller Länder in Asien abruft.
   
     ```sql
     SELECT name, capital FROM country WHERE continent = 'Asia';
     ```

6. **Übung 3: Abfrage nach Fläche**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die die Namen und Flächen aller Länder abruft, deren Fläche größer als 1 Million Quadratkilometer ist.
   
     ```sql
     SELECT name, area FROM country WHERE area > 1000000;
     ```

7. **Übung 4: Abfrage nach Regierungsform**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die den Namen und die Regierungsform aller Länder abruft, die eine Republik sind.
   
     ```sql
     SELECT name, government FROM country WHERE government = 'Republic';
     ```

## Teil 3: Erweiterte Übungen

8. **Übung 5: Kombinierte Bedingungen**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die den Namen, die Bevölkerung und die Fläche aller Länder abruft, die in Afrika liegen und deren Bevölkerung größer als 20 Millionen ist.
   
     ```sql
     SELECT name, population, area FROM country WHERE continent = 'Africa' AND population > 20000000;
     ```

9. **Übung 6: Sortierung und Einschränkung**

   - **Aufgabe:** Schreibe eine SQL-Abfrage, die die Namen aller Länder abruft, die in Südamerika liegen, und sortiere sie nach ihrer Fläche in aufsteigender Reihenfolge.
   
     ```sql
     SELECT name FROM country WHERE continent = 'South America' ORDER BY area ASC;
     ```

10. **Übung 7: Textsuche**

    - **Aufgabe:** Schreibe eine SQL-Abfrage, die alle Länder abruft, deren Name mit dem Buchstaben 'A' beginnt.
    
      ```sql
      SELECT * FROM country WHERE name LIKE 'A%';
      ```

## Abschluss

- **Hausaufgabe:** Wende die erlernten SQL-Befehle an, um eigene Abfragen zu erstellen. Notiere mindestens drei eigene Abfragen und bringe sie zur nächsten Unterrichtsstunde mit.
*/

/*markdown

*/