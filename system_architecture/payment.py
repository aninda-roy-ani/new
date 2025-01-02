class Payment:
    def __init__(self, payment_id, member, amount, payment_method, date):
        self.__payment_id = payment_id
        self.__member = member
        self.__amount = amount
        self.__payment_method = payment_method
        self.__date = date

    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_member(self):
        return self.__member

    def set_member(self, member):
        self.__member = member

    def get_amount(self):
        return float(self.__amount)

    def set_amount(self, amount):
        self.__amount = amount

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date
