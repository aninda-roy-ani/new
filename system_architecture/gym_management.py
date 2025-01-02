from system_architecture.appointment import Appointment
from system_architecture.attendance import Attendance
from system_architecture.gym_location import GymLocation
from system_architecture.gym_manager import GymManager
from system_architecture.member import Member
from system_architecture.payment import Payment
from system_architecture.subscription import Subscription
from system_architecture.workout_zone import WorkoutZone


class GymManagement:
    def __init__(self):
        self.__gyms = []

    def add_gym(self, gym):
        if isinstance(gym, GymLocation):
            self.__gyms.append(gym)
        else:
            raise ValueError("Only GymLocation instances can be added")

    def get_gyms(self):
        return self.__gyms

    def find_gym_by_id(self, location_id):
        for gym in self.__gyms:
            if gym.get_location_id() == location_id:
                return gym
        return None

    def remove_gym(self, location_id):
        gym = self.find_gym_by_id(location_id)
        if gym:
            self.__gyms.remove(gym)

    def gym(self, gym_id, city, manager):
        return GymLocation(location_id=gym_id, city=city, gym_manager=manager)

    def gym_manager(self, gym_id, manager_name, manager_contact):
        return GymManager(manager_id=gym_id, name=manager_name, contact=manager_contact)

    def workout_zone(self, zone_id, exercise_type, attendant):
        return WorkoutZone(zone_id=zone_id, exercise_type=exercise_type, attendant=attendant)

    def member(self, member_id, personal_details, health_info, membership_status):
        return Member(member_id=member_id, personal_details=personal_details, health_info=health_info,
                      membership_status=membership_status)

    def appointment(self, appointment_id, member_id, trainer, appointment_type, schedule):
        return Appointment(appointment_id=appointment_id, member=member_id, trainer=trainer,
                           appointment_type=appointment_type, schedule=schedule)

    def payment(self, payment_id, member_id, amount, payment_method, date):
        return Payment(payment_id=payment_id, member=member_id, amount=amount, payment_method=payment_method,
                date=date)

    def subscription(self, subscription_id, member_id, plan_type, start_date, end_date):
        return Subscription(subscription_id=subscription_id, member=member_id, plan_type=plan_type,
                                            start_date=start_date, end_date=end_date)

    def attendance(self, attendance_id, member_id, date, activity):
        return Attendance(attendance_id=attendance_id, member=member_id, date=date, activity=activity)

