class Attendance:
    def __init__(self, attendance_id, member, date, activity):
        self.__attendance_id = attendance_id
        self.__member = member
        self.__date = date
        self.__activity = activity

    def get_attendance_id(self):
        return self.__attendance_id

    def set_attendance_id(self, attendance_id):
        self.__attendance_id = attendance_id

    def get_member(self):
        return self.__member

    def set_member(self, member):
        self.__member = member

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_activity(self):
        return self.__activity

    def set_activity(self, activity):
        self.__activity = activity
