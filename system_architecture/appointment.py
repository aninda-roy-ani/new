class Appointment:
    def __init__(self, appointment_id, member, trainer, appointment_type, schedule):
        self.__appointment_id = appointment_id
        self.__member = member
        self.__trainer = trainer
        self.__appointment_type = appointment_type
        self.__schedule = schedule

    def get_appointment_id(self):
        return self.__appointment_id

    def set_appointment_id(self, appointment_id):
        self.__appointment_id = appointment_id

    def get_member(self):
        return self.__member

    def set_member(self, member):
        self.__member = member

    def get_trainer(self):
        return self.__trainer

    def set_trainer(self, trainer):
        self.__trainer = trainer

    def get_appointment_type(self):
        return self.__appointment_type

    def set_appointment_type(self, appointment_type):
        self.__appointment_type = appointment_type

    def get_schedule(self):
        return self.__schedule

    def set_schedule(self, schedule):
        self.__schedule = schedule
