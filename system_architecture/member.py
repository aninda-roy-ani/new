class Member:
    def __init__(self, member_id, personal_details, health_info, membership_status):
        self.__member_id = member_id
        self.__personal_details = personal_details
        self.__health_info = health_info
        self.__membership_status = membership_status

    def get_member_id(self):
        return self.__member_id

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def get_personal_details(self):
        return self.__personal_details

    def set_personal_details(self, personal_details):
        self.__personal_details = personal_details

    def get_health_info(self):
        return self.__health_info

    def set_health_info(self, health_info):
        self.__health_info = health_info

    def get_membership_status(self):
        return self.__membership_status

    def set_membership_status(self, membership_status):
        self.__membership_status = membership_status
