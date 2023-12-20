# Feiertags Kalender

Dieses ist ein kleines Projekt zum Neujahres Event 2023 vom Discord Server DevCloud.

Der Sinn beim Event ist es zum Jahres Ende etwas kleines zu Coden, am besten passt es zum Thema.

Ich habe mich hierbei bei den Ideen bedient, Idee 1

> Idee: Schreibe ein Programm, welches dir mitteilt, wann die nächsten Feiertage(Neujahr, Karfreitag, Tag der Arbeit, Weihnachten, ...) sind und in welchen Bundesland diese gefeiert werden.

Dieses Projekt habe ich hiermit in diesen Repo umgesetzt.

---

# Nutzung
*es sollte beachtet werden das Python so gestartet wird wie auf dem Host System es üblich ist, es kann dadurch abweichungen bei den Angaben geben*

*man muss sich mit dem Terminal im selben Ordner befinden wie die Python Skripte, um die Befehle, so weit wie unten angegeben, ausführen zu können*

### Öffnen der Einstellungen
Zum Öffnen der einstellungen muss die app.py mit dem Parameter ``settings`` gestartet werden oder die ``settings.py`` direkt.

**Wenn Parameter**

````bash
python app.py settings
````

**Wenn Settings.py**

````bash
python settings.py
````

Sobald die Einstellungen gespeichert werden, erstellt sich eine ``settings.json`` im gleichen Verzeichnis.
Sollten alle Einstellungen standard sein, wird das Programm wird die Datei löschen.

### Allgemeines starten des Programms
Um das Programm allgemein zu starten, kann man dieses entweder über die ``app.py`` oder über die ``runner.py`` machen.
Damit das Programm mit den Einstellungen arbeiten kann muss die ``settings.json`` im selben Verzeichnis liegen wie die
auszuführenden Skripte.

**Wenn app.py**
````bash
python app.py
````

**Wenn runner.py**
````bash
python runner.py
````
---

# Funktionsweise

## Feiertagsermittlung
Zum Ermitteln der Feiertage wurde nicht direkt auf das Internet zurückgegriffen, alle Feiertage welche verschiebungen haben werden lokal berechnet.
Die anderen Feiertage sind fest geschrieben.
Alle Feiertage können mit einer angegebenen Jahreszahl berechnet werden.

Für die allgemeine Datumsverwaltung nutze ich das Datetime modul aus Python.

## App.py
Wie man oben bei der Nutzung sieht, ist es möglich jedes Modul separat anzusteuern. Die App.py ist zusammen mit dem ``argument_handler.py`` nur eine Brücke für das Aufrufen.

---
# LICENSE

Das Projekt wird unter der MIT-License laufen.

Das Bild ``calender.svg`` wurde lizenziert unter der MIT-Lizenz, gefunden habe ich es auf [SVGRepo](https://www.svgrepo.com/svg/337698/calendar-thirty-two).

---

## Das Projekt ist noch in entwicklung und nicht final, eine erste nutzbare Version wird durch einen GitHub Release veröffentlicht 
