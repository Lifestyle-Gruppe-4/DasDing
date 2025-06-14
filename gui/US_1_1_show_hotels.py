# gui/us1_1_show_hotels_by_city.py
import os, sys, PySimpleGUI as sg

# 1) Projekt-Root ins sys.path schieben, damit Imports funktionieren
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 2) Business-Logic importieren
from business_logic.hotel_manager import HotelManager
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess

def main():
    sg.theme("LightGrey1")

    # DB-Pfad
    db_path = os.path.join(project_root, 'database', 'hotel_sample.db')

    # DAL & Manager
    room_dal  = RoomDataAccess(db_path)
    hotel_dal = HotelDataAccess(db_path, room_dal)
    manager   = HotelManager(hotel_dal)

    # Layout
    layout = [
        [sg.Text("US 1.1: Hotels in einer Stadt durchsuchen", font=(None,14,'bold'))],
        [sg.Text("Stadt:"), sg.Input(key="-CITY-", size=(20,1)), sg.Button("Anzeigen")],
        [sg.Table(
            values=[],
            headings=["Name","Adresse","Sterne"],
            key="-TABLE-",
            auto_size_columns=True,
            num_rows=10,
            expand_x=True, expand_y=True
        )],
        [sg.Button("Zurück")]
    ]

    window = sg.Window("Hotels nach Stadt", layout, size=(600,400), resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Zurück"):
            break
        if event == "Anzeigen":
            city = values["-CITY-"].strip()
            hotels = manager.find_by_city(city)
            data = [
                [h.name, f"{h.address.street}, {h.address.city} {h.address.zip_code}", h.stars]
                for h in hotels
            ]
            window["-TABLE-"].update(values=data)

    window.close()

if __name__ == "__main__":
    main()
