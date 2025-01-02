class GymManager:
    def __init__(self, manager_id, name, contact):
        self.__manager_id = manager_id
        self.__name = name
        self.__contact = contact

    def get_manager_id(self):
        return self.__manager_id

    def set_manager_id(self, manager_id):
        self.__manager_id = manager_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact
