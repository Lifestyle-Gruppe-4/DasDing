# Projekt: Hotelreservierungssystem  
**Modul:** Anwendungsentwicklung mit Python  
**Studiengang:** BSc Business Artificial Intelligence  
**Semester:** Frühling 2025  
**Gruppe:** Gruppe 4 (DasDing)
**Gruppenmitglieder** Thomas Bartels, Silian Gyger, Michele Lepori, Simon Manger


##  1. Projektmanagement und Dokumentation

###  Projektziel  
Ziel war es, ein voll funktionsfähiges Hotelreservierungssystem zu entwickeln, welches auf Python basiert. Die Projektarbeit erfolgte iterativ anhand definierter User Stories in mehreren Sprints.

###  Zeitplanung  
Das Projekt wurde gemäss dem Semesterplan (siehe [Semesterprogramm PDF](./BAI%20Semesterprogramm%20AEP%202025%20v2.pdf)) durchgeführt.  
Die Sprintstruktur war wie folgt:
- **Sprint 0:** Setup, Teambildung, GitHub/Deepnote
- **Sprint 1–2:** Grundlagen, OOP, erste User Stories
- **Sprint 3:** Datenbankanbindung, Logik
- **Sprint 4:** Visualisierung, Erweiterungen, Doku

Alle Tasks wurden im GitHub-Project Board geplant und verwaltet.

###  Zusammenarbeit  
- GitHub wurde für Task-Zuweisung, Issues und Reviews genutzt  
- Deepnote und MS Teams dienten als Plattform für Kommunikation und Dokumentation  
- Alle Gruppenmitglieder waren durchgängig aktiv beteiligt  
- Wöchentliche Sprint Reviews und Coachings wurden durchgeführt

---

##  2. Technische Umsetzung

###  Architekturübersicht
- **models/**: Python-Klassen (Hotel, Zimmer, Buchung etc.)  
- **managers/**: Geschäftslogik (z. B. Buchungslogik, Admin-Funktionen)  
- **database/**: Verbindung und Methoden für SQLite  
- **ui/**: Konsolen-Interface zur Benutzerinteraktion  

###  Umsetzung von User Stories

####  Minimale User Stories (Auswahl)
- Suche nach Hotels nach Stadt, Sterne, Verfügbarkeit, Gästezahl
- Anzeige von Hotel- und Zimmerdetails
- Zimmerbuchung inkl. Rechnungserstellung
- Buchungsstornierung

####  Erweiterte User Stories (mit DB-Schemaänderung)
- Hotelbewertungen abgeben & lesen (`Reviews`-Tabelle)
- Buchungshistorie für Gäste

####  User Story mit Datenvisualisierung
- **Auslastung pro Zimmertyp** mittels Deepnote Charts  
  Beispiel: Balkendiagramm zur Darstellung gebuchter Zimmer je Typ

---

##  3. Kommunikation und Informationen

-  **GitHub Project Board** zur Organisation  
-  **MS Teams** zur Abstimmung & Diskussion  
-  **Deepnote Notebooks** für Demos und Visualisierung  
-  **README.md** & Code-Kommentare (Docstrings) für Dokumentation  

---

##  4. Dokumentationsstruktur

- Übersicht und Planung
- Technische Beschreibung (Architektur, Struktur)
- Umgesetzte User Stories
- Datenmodell (Klassendiagramm via Visual Paradigm)
- Beispiel-Charts und SQL-Queries
- Screenshots & Code-Snippets
- Lessons Learned & Ausblick

---

##  5. Design & Erscheinungsbild

- Klar strukturierte Markdown-Datei
- Diagramme, Charts und Screenshots zur Visualisierung
- Einheitliche Formatierung mit GitHub-Flair
- Optional: PDF-Version dieser Dokumentation via Deepnote oder Pandoc

---

##  6. Projektmanagement mit GitHub Board

Das Project Board enthielt:
- **User Story-Tickets** mit Beschreibung und Subtasks
- Zuweisung an Gruppenmitglieder
- Statusspalten: `To Do → In Progress → Done`


