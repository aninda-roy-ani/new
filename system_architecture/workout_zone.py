class WorkoutZone:
    def __init__(self, zone_id, exercise_type, attendant):
        self.__zone_id = zone_id
        self.__exercise_type = exercise_type
        self.__attendant = attendant
        self.__updates = []
        self.__schedules = []
        self.__promotions = []

    def get_zone_id(self):
        return self.__zone_id

    def set_zone_id(self, zone_id):
        self.__zone_id = zone_id

    def get_exercise_type(self):
        return self.__exercise_type

    def set_exercise_type(self, exercise_type):
        self.__exercise_type = exercise_type

    def get_attendant(self):
        return self.__attendant

    def set_attendant(self, attendant):
        self.__attendant = attendant

    def add_update(self, update):
        self.__updates.append(update)

    def get_updates(self):
        return self.__updates

    def add_schedule(self, schedule):
        self.__schedules.append(schedule)

    def get_schedules(self):
        return self.__schedules

    def add_promotion(self, promotion):
        self.__promotions.append(promotion)

    def get_promotions(self):
        return self.__promotions
