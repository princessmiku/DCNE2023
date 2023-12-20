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
Zum Öffnen der einstellungen muss die app.py mit dem Parameter ``settings`` gestartet werden.

````bash
python app.py settings
````

Sobald die Einstellungen gespeichert werden, erstellt sich eine ``settings.json`` im gleichen Verzeichnis im Ordner `data`.
Sollten alle Einstellungen standard sein, wird das Programm wird die Datei löschen.

### Allgemeines starten des Programms
Um das Programm allgemein zu starten muss man die ``app.py`` ausführen
Damit das Programm mit den Einstellungen arbeiten kann, muss sich der ``data`` Ordner im selben verzeichnis befinden wie das auszuführende Skript.

````bash
python app.py
````

### Starten der GUI
Es ist möglich eine Allgemeine ansicht für die Feiertage anzuzeigen, dafür nutzt man den parameter ``gui``
````bash
python app.py gui
````


### Autostart

Lege das Skript in deinen autostart, um es automatisch beim System start starten zu lassen. Dabei ist zu beachten das
man das Programm ohne Parameter startet.

- [Windows 10/11 (MediaMarkt)](https://www.mediamarkt.de/de/content/themen-specials/schon-gewusst-wie/windows-10-autostart-programme-entfernen-hinzufuegen) unter dem Punkt ``Mithilfe von „Ausführen“``


---

# Funktionsweise

## Feiertagsermittlung
Zum Ermitteln der Feiertage wurde nicht direkt auf das Internet zurückgegriffen, alle Feiertage welche verschiebungen haben werden lokal berechnet.
Die anderen Feiertage sind fest geschrieben.
Alle Feiertage können mit einer angegebenen Jahreszahl berechnet werden.

Für die allgemeine Datumsverwaltung nutze ich das Datetime modul aus Python.

## App.py

Die App.py dient der ansteuerung der Module, eine einzelne ansteuerung der Module war möglich, wurde aber nun aus Kosten der besseren Ordner Struktur entfernt.

---
# LICENSE

Das Projekt wird unter der MIT-License laufen.

Das Bild ``calender.svg`` wurde lizenziert unter der MIT-Lizenz, gefunden habe ich es auf [SVGRepo](https://www.svgrepo.com/svg/337698/calendar-thirty-two).

---

## Das Projekt ist noch in entwicklung und nicht final, eine erste nutzbare Version wird durch einen GitHub Release veröffentlicht 
