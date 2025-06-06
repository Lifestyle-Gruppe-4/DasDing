# Projekt: Hotelreservierungssystem  
**Modul:** Anwendungsentwicklung mit Python  
**Studiengang:** BSc Business Artificial Intelligence  
**Semester:** Frühling 2025  
**Gruppe:** Gruppe 4 (DasDing)  
**Gruppenmitglieder:** Thomas Bartels, Silian Gyger, Michele Lepori, Simon Manger  



##  1. Projektmanagement und Dokumentation

###  Projektziel  
Ziel dieses Projekts war die schrittweise Konzeption und Entwicklung eines funktionsfähigen **Hotelreservierungssystems** mithilfe der Programmiersprache Python. Das System sollte es Gästen ermöglichen, gezielt nach Hotels und verfügbaren Zimmern zu suchen, Buchungen vorzunehmen sowie Rechnungen zu generieren. Gleichzeitig sollten Administratoren in der Lage sein, die Stammdaten der Hotels und Zimmer effizient zu verwalten. Diese Anforderungen wurden uns gemäss der vordefinierten User Storys mitgegeben. 

Das Projekt war im Rahmen des Moduls *Anwendungsentwicklung mit Python* eingebettet, das projektbasiertes Lernen mit schrittweiser Einführung in Programmierkonzepte kombiniert. Die Umsetzung orientierte sich an vordefinierten User Stories, die reale Anwendungsfälle aus dem Bereich der Hotelbuchung abbilden. Diese decken sowohl grundlegende Funktionen (z. B. Hotelsuche, Buchung, Rechnung) als auch fortgeschrittene Anforderungen (z. B......) ab.

Ein besonderes Augenmerk lag auf folgenden Zielen:
- Anwendung der erlernten Python-Konzepte in einem realistischen Szenario
- Arbeiten mit objektorientierter Programmierung, Datenbanken (SQLite) und Pycharm
- Agile Projektorganisation in mehreren Iterationen (Sprints)
- Dokumentation und Präsentation des Projekts mit Tools wie GitHub, MS-Teams und Deepnote

Durch diese praxisnahe Projektarbeit konnten wir nicht nur unsere technischen Fähigkeiten mit Python festigen, sondern auch wertvolle Erfahrung im Bereich Teamarbeit und Projektmanagement sammeln.

###  Zeitplanung  
Das Projekt wurde iterativ in mehreren Sprints gemäss dem Semesterplan (siehe [Semesterprogramm PDF](./BAI%20Semesterprogramm%20AEP%202025%20v2.pdf)) durchgeführt.  
Die Sprintstruktur war wie folgt:
- **Sprint 0:** Setup, Teambildung, GitHub/Deepnote
- **Sprint 1–2:** Grundlagen, OOP, erste User Stories
- **Sprint 3:** Datenbankanbindung, Logik
- **Sprint 4:** Visualisierung, Erweiterungen, Doku

Alle Tasks wurden im GitHub-Project Board geplant und verwaltet.

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
- .... ?? Hotelbewertungen abgeben & lesen (`Reviews`-Tabelle)
- Buchungshistorie für Gäste

####  User Story mit Datenvisualisierung
- ....?? **Auslastung pro Zimmertyp** mittels Deepnote Charts  
  Beispiel: Balkendiagramm zur Darstellung gebuchter Zimmer je Typ

#### Vorgehen 
.... Erklärung der Layers etc.

---

##  3. Kommunikation und Informationen

-  **GitHub Project Board** zur Organisation, für Task-Zuweisung, Issues und Reviews genutzt 
-  **MS Teams** zur Abstimmung, Diskussion, und Video-Aufnahme 
-  **Deepnote Notebooks** hilfreich für Analysen, Demos, Abbidung der verschiedenen Layers, Datenabfragen und Abbildung der User Storys.
-  **Visual Paradigm** für die Erstellung der Klassen
-  **README.md** für Dokumentation
-  **Whatsapp** diente zur Kordination untereinander und zur Info wer wann Änderungen gepushed hat.
  
- Alle Gruppenmitglieder waren durchgängig aktiv beteiligt, present bei den Coachings. 
- Wöchentliche Sprint Reviews und Coachings wurden durchgeführt


---

##  4. Projektmanagement mit GitHub Board

Das Project Board enthielt:
- **User Story-Tickets** mit Beschreibung und Subtasks
- Zuweisung an Gruppenmitglieder
- Statusspalten: `To Do → In Progress → Done`

---

## Fazit & Lessons Learned

Was wir erreicht haben

- Entwicklung eines funktionierenden Hotelreservierungssystems mit Python
- Umsetzung zahlreicher User Stories – von der Hotelsuche bis zur Rechnungserstellung
- Anwendung objektorientierter Konzepte, Datenbankintegration und Datenvisualisierung
- Erfolgreiche Zusammenarbeit in einem agilen, sprintbasierten Projektsetting
- Einsatz Tools wie GitHub, Deepnote, SQLite, Visual Paradigm und Pycharm

### Was wir gelernt haben

-  Die Trennung von Datenmodell, Geschäftslogik und Benutzeroberfläche vereinfacht die Wartung
-  Frühe Strukturierung des Codes und der User Stories vermeidet unnötige Refactorings
-  Iteratives Arbeiten mit Feedback-Schleifen steigert die Qualität und Teamproduktivität
-  Klare Kommunikation im Team über MS Teams und das Project Board war hilfreich
- Es hat geholfen die Aufgaben zusammen zu besprechen, in den Coaching Sessions zusammen weiterzuarbeiten und danach die restlichen Aufgaben aufzuteilen. Ausserdem war es gut, dass wir stets vor Ort waren. Das hat die Koordination und Zusammenarbeit vereinfacht. 





