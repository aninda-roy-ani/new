class StaffManagementDashboard:
    def __init__(self, manager):
        self.__manager = manager
        self.__reports = []

    def get_manager(self):
        return self.__manager

    def set_manager(self, manager):
        self.__manager = manager

    def add_report(self, report):
        self.__reports.append(report)

    def get_reports(self):
        return self.__reports
