# Projekt: Hotelreservierungssystem  
**Modul:** Anwendungsentwicklung mit Python  
**Studiengang:** BSc Business Artificial Intelligence  
**Semester:** Frühling 2025  
**Gruppe:** Gruppe 4 (DasDing)  
**Gruppenmitglieder:** Thomas Bartels, Silian Gyger, Michele Lepori, Simon Manger  



##  1. Projektmanagement und Dokumentation

###  Projektziel  
Ziel dieses Projekts war die schrittweise Konzeption und Entwicklung eines funktionsfähigen **Hotelreservierungssystems** mithilfe der Programmiersprache Python. Das System sollte es Gästen ermöglichen, gezielt nach Hotels und verfügbaren Zimmern zu suchen, Buchungen vorzunehmen sowie Rechnungen zu generieren. Gleichzeitig sollten Administratoren in der Lage sein, die Stammdaten der Hotels und Zimmer effizient zu verwalten. Diese Anforderungen wurden uns gemäss der vordefinierten User Storys mitgegeben. 

Das Projekt war im Rahmen des Moduls *Anwendungsentwicklung mit Python* eingebettet, das projektbasiertes Lernen mit schrittweiser Einführung in Programmierkonzepte kombiniert. Die Umsetzung orientierte sich an vordefinierten User Stories, die reale Anwendungsfälle aus dem Bereich der Hotelbuchung abbilden. Diese decken sowohl grundlegende Funktionen (z. B. Hotelsuche, Buchung, Rechnung) als auch fortgeschrittene Anforderungen (z. B Bewertungen nach Aufenthalt, Anpassungen von Stammdaten) ab.

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
- **Model Layer: model/**: Python-Klassen (Hotel, Zimmer, Buchung etc.)  
- **Logic Layer: business_logic/**: Geschäftslogik (z. B. Buchungslogik, Admin-Funktionen)  
- **Data Layer: data_access/**: Verbindung und Methoden für SQLite  
- **Presentation Layer: ui/**: Konsolen-Interface zur Benutzerinteraktion  

###  Umsetzung von User Stories

####  Minimale User Stories (Auswahl)
- Suche nach Hotels nach Stadt, Sterne, Verfügbarkeit, Gästezahl
- Anzeige von Hotel- und Zimmerdetails
- Zimmerbuchung inkl. Rechnungserstellung
- Buchungsstornierung

####  Erweiterte User Stories (mit DB-Schemaänderung)
- Hotelbewertungen nach Aufenthalt abgeben (`Reviews`-Tabelle)
- Hotelbewertungen pro Hotel anschauen
- Rechnungsstatus auf "Bezahlt" stellen können

####  User Story mit Datenvisualisierung
- Anzahl Buchungen pro Hotel 
- Duchschnittlicher Zimmerpreis pro Hotel
- Buchungen pro Zimmertyp in einem Hotel

#### Vorgehen 
Zu Beginn des Projekts haben wir uns intensiv mit den Grundlagen der Python-Programmierung beschäftigt sowie die verwendeten Tools wie Deepnote, GitHub und PyCharm eingerichtet. Danach wurde gemeinsam ein Klassendiagramm in Visual Paradigm erstellt, um die Datenbankstruktur und die logischen Entitäten festzulegen.

Basierend auf diesem Klassendiagramm wurden die Model-Klassen zuerst in Deepnote erstellt. Anschliessend haben wir in der gleichen Umgebung auch den Data Access Layer (DAL) sowie den Business Logic Manager implementiert. Erste einfache User Stories wie „Hotel hinzufügen“ oder „Zimmer anzeigen“ wurden direkt in Deepnote getestet, um die Interaktion zwischen den Schichten zu verifizieren.

Als nächster Schritt wurde die gesamte Struktur in PyCharm nachgebildet, um komplexere Imports und Dateiabhängigkeiten korrekt abzubilden. In PyCharm testeten wir nacheinander alle User Stories und passten die Business-Logik sowie Datenbankabfragen entsprechend an. Sobald diese erfolgreich funktionierten, wurden sie wieder zurück in Deepnote-Notebooks übertragen und dort mit erklärendem Text dokumentiert.

Im Verlauf des Projekts mussten einzelne User Stories sowie Klassen und Layers nochmals angepasst werden, da sich durch Anforderungen oder neue Erkenntnisse Änderungen am Datenbankschema ergaben. Diese Änderungen wurden iterativ vorgenommen.

Zum Abschluss haben wir Visualisierungen mit dem "Charts"-Block in Deepnote erstellt, z. B. um die Buchungen pro Zimmertyp in einem Hotel oder der durchschnittliche Zimmerpreis pro Hotel darzustellen. Die entsprechenden Daten wurden zuvor mit SQL-Abfragen ausgelesen, in einem Pandas DataFrame gespeichert und dann grafisch aufbereitet.

---

##  3. Kommunikation und Informationen

-  **GitHub Project Board** zur Organisation, für Task-Zuweisung, Issues und Reviews genutzt 
-  **MS Teams** für kurze Absprachen, Neuigkeiten und Infos zum individuellen Fortschritt, und Video-Aufnahme. 
-  **Deepnote Notebooks** hilfreich für Analysen, Demos, Abbidung der verschiedenen Layers, Datenabfragen und Abbildung der User Storys.
-  **Visual Paradigm** für die Erstellung der Klassen
-  **README.md** für Dokumentation
-  **Whatsapp** diente zur Koordination untereinander und zur Info wer wann Änderungen gepushed hat.
  
- Alle Gruppenmitglieder waren durchgängig aktiv beteiligt und present bei den Coachings. 
- Wöchentliche Sprint Reviews und Coachings wurden durchgeführt


---

##  4. Projektmanagement mit GitHub Board

Das Project Board enthielt:
- Zu erledigende Aufgaben mit Beschreibung und Subtasks
- Zuweisung an Gruppenmitglieder
- Statusspalten: `To Do → In Progress → Done`
- Backlog

---

## 5. Themenaufteilung

Zu Beginn unseres Projektes haben wir die Modellierung der wichtigsten Klassen untereinander aufgeteilt:
- Silian Gyger: Facility und Guest
- Simon Manger: Room und RoomType
- Michele Lepori: Hotel und Address
- Thomas Bartels: Booking und Invoice

Auch die User Stories haben wir klar unter uns verteilt:
- Silian Gyger: User Stories 1 und 2
- Simon Manger: User Stories 3 und 4
- Thomas Bartels: User Stories 5, 6 und 7
- Michele Lepori: User Stories 8, 9 und 10

Anfangs hat jeder an seinen eigenen Aufgaben gearbeitet. Doch je näher das Projekt dem Ende kam, desto mehr haben wir uns gegenseitig unterstützt - sei es beim Programmieren, Testen oder Kontrollieren. Unere Zusaammenarbeit wurde dadurch deutlich agiler, was sich positiv auf die Qualität und den Teamgeist ausgewirkt hat.

---

## 6. Ausführung der Notebooks in Deepnote & Python Files
### Deepnote
Das Notebook sollten von oben nach unten in der angegebenen Reihenfolge ausgeführt werden. Am wichtigsten ist der erste Codeblock - dort werden alle notwendigen Bibliotheken importiert und die Datenbankverbindungen aufgebaut. Ohne dieses Block funktionieren die anderen Blöcke nicht. Für jede User Story gibt es einen eigenen Code-Block mit einer kurzen Beschreibung, wie es ausgeführt werden soll. So kann man gezielt einzelne Funktionen nachvollziehen und testen.

### Python
Im Ordner "ui" befinden sich mehrere Python-Dateien, die nach den jeweiligen User-Story-Nummern benannt sind (z.B. user_stroy_1, user_story_2 usw.) Jede Datei enthält den Code für ein bestimmte User Story. Diese Dateien lassen sich unabhängig voneinander ausführen. Man kann sie direkt in der Konsole starten, um die jeweiligen Funktionen zu testen oder zu überprüfen, ob alles korrekt funktioniert.

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

  
## Reflexion

Im Verlauf des Projekts haben wir:
- Unsere Kenntnisse in objektorientierter Programmierung (OOP) in Python vertieft
- Eine saubere Layered Architecture mit klarer Trennung von Datenzugriff, Logik und UI umgesetzt
- Den Umgang mit SQLite, komplexeren SQL-Abfragen und deren Einbindung in eigene Python-Klassen geübt
- Die Arbeit im Team mithilfe von GitHub-Projekten, Pull Requests und Deepnote effektiv koordiniert
- Konzepte wie dynamische Preisberechnung, Validierung von Eingaben und Zustandsverwaltung praktisch angewendet

Das Projekt war ein wertvoller Schritt in Richtung praxisnaher Softwareentwicklung mit Python und hat uns gezeigt, wie wichtig Struktur, Planung und saubere Zusammenarbeit sind.

---
## Einsatz von unterstützenden Tools

Während der Entwicklung haben wir ChatGPT punktuell zur Unterstützung verwendet, für:

- Zur Klärung von spezifischen Syntax-Fragen in Python (z. B. zu datetime, Fehlerbehandlung, Importproblemen)
- Beim Debugging und zur Überprüfung von typischen Fehlerquellen in DAL- oder Manager-Klassen
- Für Anregungen zur Kürzung oder Strukturierung von Funktionen

 Chatgpt wurde nicht als Ersatz für eigene Arbeit, sondern als Ergänzung genutzt 

## Projektlinks
Deepnote-Projekt
Github Repository
Github Project Board





