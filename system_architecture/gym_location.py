class GymLocation:
    def __init__(self, location_id, city, gym_manager):
        self.__location_id = location_id
        self.__city = city
        self.__gym_manager = gym_manager
        self.__workout_zones = []
        self.__members = []
        self.__appointments = []
        self.__payments = []
        self.__subscriptions = []
        self.__attendance_records = []

    def get_location_id(self):
        return self.__location_id

    def get_city(self):
        return self.__city

    def get_gym_manager(self):
        return self.__gym_manager

    def get_workout_zones(self):
        return self.__workout_zones

    def add_workout_zone(self, workout_zone):
        self.__workout_zones.append(workout_zone)

    def get_members(self):
        return self.__members

    def add_member(self, member):
        self.__members.append(member)

    def get_appointments(self):
        return self.__appointments

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    def get_payments(self):
        return self.__payments

    def add_payment(self, payment):
        self.__payments.append(payment)

    def get_subscriptions(self):
        return self.__subscriptions

    def add_subscription(self, subscription):
        self.__subscriptions.append(subscription)

    def get_attendance(self):
        return self.__attendance_records

    def add_attendance(self, attendance):
        self.__attendance_records.append(attendance)
