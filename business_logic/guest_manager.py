from typing import Dict, List, Optional
from model.guest import Guest
from model.address import Address,addr1, addr2, addr3

class GuestManager:

    #Business-Logic-Klasse zum Verwalten von Gast-Objekten.

    def __init__(self):
        self._guests: Dict[int, Guest] = {}

    def create_guest(self,
                     guest_id: int,
                     first_name: str,
                     last_name: str,
                     email: str,
                     address: Address) -> Guest:

        #Erstellt einen neuen Gast und speichert ihn im Manager.

        if guest_id in self._guests:
            raise ValueError(f"Guest with id {guest_id} already exists.")
        guest = Guest(guest_id, first_name, last_name, email, address)
        self._guests[guest_id] = guest
        return guest

    def get_guest(self, guest_id: int) -> Optional[Guest]:

        #Gibt den Gast mit gegebener ID zurück oder None, wenn nicht gefunden.

        return self._guests.get(guest_id)

    def update_guest(self,
                     guest_id: int,
                     first_name: Optional[str] = None,
                     last_name: Optional[str] = None,
                     email: Optional[str] = None,
                     address: Optional[Address] = None) -> Guest:

        #Aktualisiert Attribute eines bestehenden Gastes.

        guest = self.get_guest(guest_id)
        if guest is None:
            raise KeyError(f"No guest with id {guest_id}.")
        if first_name is not None:
            guest.first_name = first_name
        if last_name is not None:
            guest.last_name = last_name
        if email is not None:
            guest.email = email
        if address is not None:
            guest.address = address
        return guest

    def delete_guest(self, guest_id: int) -> None:

        #Entfernt einen Gast aus dem Manager.

        if guest_id not in self._guests:
            raise KeyError(f"No guest with id {guest_id}.")
        del self._guests[guest_id]

    def list_guests(self) -> List[Guest]:

        #Gibt alle erstellten Gäste zurück.

        if not self._guests:
            print("No guests yet.")
            return
        for guest in self._guests.values():
            print(f"ID: {guest.guest_id}\n"
                  f"First name: {guest.first_name}\n"
                  f"Last name: {guest.last_name}\n"
                  f"Email: {guest.email}\n"
                  f"Address: {guest.address}\n"
                  f"")



manager = GuestManager()
guest1 = manager.create_guest(1, "Silian","Gyger",email="silian.gyger@gmail.com",address=addr3)
guest2 = manager.create_guest(2, "Michele","Lepori",email="michele.lepori@el.com",address=addr2)
guest3 = manager.create_guest(3, "Thomas","Bartels",email="tm.bartels@outlook.com",address=addr1)

#print(manager.list_guests())
#print(manager.get_guest(1))
print(manager.list_guests())