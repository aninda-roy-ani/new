class Subscription:
    def __init__(self, subscription_id, member, plan_type, start_date, end_date):
        self.__subscription_id = subscription_id
        self.__member = member
        self.__plan_type = plan_type
        self.__start_date = start_date
        self.__end_date = end_date

    def get_subscription_id(self):
        return self.__subscription_id

    def set_subscription_id(self, subscription_id):
        self.__subscription_id = subscription_id

    def get_member(self):
        return self.__member

    def set_member(self, member):
        self.__member = member

    def get_plan_type(self):
        return self.__plan_type

    def set_plan_type(self, plan_type):
        self.__plan_type = plan_type

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date
