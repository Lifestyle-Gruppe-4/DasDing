from datetime import date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess


# Datenbankpfad und Initialisierung der DALs
db_path = "../database/hotel_sample.db"
address_dal = AddressDataAccess(db_path)
booking_dal = BookingDataAccess(db_path)
facility_dal = FacilityDataAccess(db_path)
guest_dal = GuestDataAccess(db_path)
invoice_dal = InvoiceDataAccess(db_path)
room_dal = RoomDataAccess(db_path)
room_type_dal = RoomTypeDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path,room_dal)

# Intialisierung der Manager
address_manager = AddressManager(address_dal)
booking_manager = BookingManager(booking_dal)
facility_manager = FacilityManager(facility_dal)
guest_manager = GuestManager(guest_dal)
invoice_manager = InvoiceManager(invoice_dal)
room_manager = RoomManager(room_dal)
room_type_manager = RoomTypeManager(room_type_dal)
hotel_manager = HotelManager(hotel_dal)

def user_story_7():
    """Dynamische Preisberechnung anzeigen"""
    try:
        hotels = hotel_manager.get_all_hotels()
        if not hotels:
            print("Keine Hotels gefunden.")
            return

        print("\nVerfügbare Hotels: ")
        for h in hotels:
            print(f" {h.hotel_id}. {h.name}")

        selection = input("\nWelche Hotels möchten Sie gerne vergleichen? (IDs mit Komma trennen): ").strip()
        try:
            ids = [int(x) for x in selection.split(",") if x.strip()]
        except ValueError:
            print("Ungültige Eingabe.")
            return

        chosen = []
        for i in ids:
            hotel = hotel_manager.find_by_id(i)
            if hotel:
                chosen.append(hotel)
            else:
                print(f"Hotel mit ID {i} nicht gefunden.")

        if not chosen:
            print("Keine gültigen Hotels ausgewählt.")
            return

        print("\nFür welche Saison möchten Sie die Preise vergleichen?")
        print("0 = Abbruch")
        print("1 = Nebensaison  (März, April, Mai, Oktober, November)")
        print("2 = Normalsaison (Januar, Juni, September)")
        print("3 = Hochsaison   (Februar, Juli, August, Dezember)")
        print("4 = Alle Saison")
        season_choice = input("\nAuswahl: ").strip()

        if season_choice == "0":
            print("Abgebrochen. Wir wünschen Ihnen einen schönen Tag.")
            return
        if season_choice not in {"1", "2", "3", "4"}:
            print("Ungültige Eingabe.")
            return

        # Zuordnung der Monate zu den Saison-Typen
        season_months = {
            "neben": [3, 4, 5, 10, 11],
            "normal": [1, 6, 9],
            "hoch": [2, 7, 8, 12],
        }

        month_names = {
            1: "Januar",
            2: "Februar",
            3: "März",
            4: "April",
            5: "Mai",
            6: "Juni",
            7: "Juli",
            8: "August",
            9: "September",
            10: "Oktober",
            11: "November",
            12: "Dezember",
        }

        year = date.today().year

        def months_to_string(month_list):
            return ", ".join(month_names[m] for m in month_list)

        for hotel in chosen:
            print(f"\nHotel: {hotel.name}")
            for room in hotel.rooms:
                base_price = room.price_per_night

                hoch_price, hoch_factor = room_manager.calculate_seasonal_price(
                    base_price, date(year, season_months["hoch"][0], 1)
                )
                neben_price, neben_factor = room_manager.calculate_seasonal_price(
                    base_price, date(year, season_months["neben"][0], 1)
                )
                normal_price, normal_factor = room_manager.calculate_seasonal_price(
                    base_price, date(year, season_months["normal"][0], 1)
                )

                print(f" Zimmer {room.room_number}")
                print(f"   Basispreis: {base_price:.2f} CHF")
                if season_choice in {"1", "4"}:
                    print(f"   Nebensaison ({months_to_string(season_months["neben"])})"
                          f"   (Faktor {neben_factor:.2f}): Preis {neben_price:.2f} CHF"
                          )
                if season_choice in {"2", "4"}:
                    print(
                        f"   Normalsaison ({months_to_string(season_months['normal'])})"
                        f" (Faktor {normal_factor:.2f}): Preis {normal_price:.2f} CHF"
                    )
                if season_choice in {"3", "4"}:
                    print(
                        f"   Hochsaison ({months_to_string(season_months['hoch'])})"
                        f" (Faktor {hoch_factor:.2f}): Preis {hoch_price:.2f} CHF"
                    )

    except Exception as e:
        print(f"Fehler: {e}")

def user_story_7_menu():
    while True:
        print("\n-- Preisgestaltung --")
        print("0 = Exit")
        print("1 = Preisgestaltung ansehen")
        choice = input("Wählen Sie eine Option (0/1): ").strip()

        if choice == "0":
            print("Auf Wiedersehen")
            break
        elif choice == "1":
            user_story_7()
        else:
            print("Ungültige Eingabe.")


user_story_7_menu()