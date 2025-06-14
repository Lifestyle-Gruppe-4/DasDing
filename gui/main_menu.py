# gui/main_menu.py
"""
Hauptmenü für alle Read-Only User-Stories
"""
import PySimpleGUI as sg

# Platzhalter-Funktion für jede User Story
# Später hier echte Implementierung aufrufen (z.B. show_hotels())
def placeholder(title):
    sg.popup(title, f"Platzhalter für: {title}", title=title)


def main():
    sg.theme("LightGrey1")

    # Layout definieren
    layout = [
        [sg.Text("Hauptmenü: Display-User-Stories", font=(None, 14, 'bold'))],
        [sg.Text("Hotels anzeigen", font=(None, 12, 'underline'), pad=(0,5))],
        [sg.Button("1.1 Alle Hotels in Stadt durchsuchen", key="US1.1")],
        [sg.Button("1.2 Hotels nach Sternen filtern", key="US1.2")],
        [sg.Button("1.3 Hotels nach Gästezahl finden", key="US1.3")],
        [sg.Button("1.4 Hotels nach Datum filtern", key="US1.4")],
        [sg.Button("1.5 Wunsch-Kombination", key="US1.5")],
        [sg.Button("1.6 Hotel-Übersicht (Name/Adresse/Sterne)", key="US1.6")],

        [sg.Text("Zimmer-Kategorien", font=(None, 12, 'underline'), pad=(0,15))],
        [sg.Button("2.1 Zimmertyp-Details anzeigen", key="US2.1")],
        [sg.Button("2.2 Nur verfügbare Zimmertypen anzeigen", key="US2.2")],

        [sg.Text("Buchungen & Preise", font=(None, 12, 'underline'), pad=(0,15))],
        [sg.Button("5. Rechnung anzeigen", key="US5")],
        [sg.Button("7. Dynamische Preise anzeigen", key="US7")],
        [sg.Button("8. Alle Buchungen anzeigen", key="US8")],

        [sg.Text("Zimmerlisten", font=(None, 12, 'underline'), pad=(0,15))],
        [sg.Button("9. Zimmerliste mit Ausstattung", key="US9")],

        [sg.HorizontalSeparator(pad=(0,15))],
        [sg.Button("Beenden", button_color=("white","firebrick"), size=(10,1))]
    ]

    window = sg.Window(
        title="Hauptmenü: Read-Only Stories",
        layout=layout,
        size=(400, 650),
        resizable=True
    )

    # Event-Loop
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Beenden"):
            break
        # Platzhalter bei Button-Events
        if event and event.startswith("US"):
            placeholder(event)

    window.close()

if __name__ == "__main__":
    main()

