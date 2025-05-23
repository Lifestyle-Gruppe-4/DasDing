from model.address import Address


class Guest:
    def __init__(self, guest_id:int, first_name:str, last_name:str, email:str, address:Address):
        if guest_id is not None and guest_id < 0:
            raise ValueError("guest ID must be postive if provided")
        if not first_name:
            raise ValueError("first name is required")
        if not last_name:
            raise ValueError("last name is required")
        if not email:
            raise ValueError("email is required")
        if not address:
            raise ValueError("address is required")

        self.__guest_id:int = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address = address

    def __repr__(self):
        return (f" ID: {self.guest_id}\n"
                f" Firstname: {self.first_name}\n"
                f" Lastname: {self.last_name}\n"
                f" Email: {self.email}\n"
                f" Adsress: {self.address}")

    @property
    def guest_id(self)-> int:
        return self.__guest_id

    @property
    def first_name(self)-> str:
        return self.__first_name

    @property
    def last_name(self)-> str:
        return self.__last_name

    @property
    def email(self)-> str:
        return self.__email

    @property
    def address(self)-> Address:
        return self.__address

    @first_name.setter
    def first_name(self, first_name:str):
        if not first_name:
            raise ValueError("first name is required")
        if not isinstance(first_name, str):
            raise ValueError("first name must be a string")
        self.__first_name = first_name
    @last_name.setter
    def last_name(self, last_name:str):
        if not last_name:
            raise ValueError("last name is required")
        if not isinstance(last_name, str):
            raise ValueError("last name must be a string")
        self.__last_name = last_name
    @email.setter
    def email(self, email:str):
        if not email:
            raise ValueError("email is required")
        if not isinstance(email, str):
            raise ValueError("email must be a string")
        self.__email = email
    @address.setter
    def address(self, address:Address):
        if not address:
            raise ValueError("address is required")
        self.__address = address


