import tkinter as tk
from tkinter import messagebox, ttk
import csv
import matplotlib.pyplot as plt
from system_architecture.gym_management import GymManagement


class GymManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.root.geometry("1200x600")
        self.root.configure(bg='black')

        self.gym_management = GymManagement()
        self.history = []

        self.saved_gym = None
        self.saved_zone = None

        self.menu_frame = tk.Frame(self.root, bg='yellow', width=200)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.create_nav_buttons()

        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.update_main_frame("Welcome to the St Mary's Fitness Gym Management System!")

    def create_nav_buttons(self):
        nav_buttons = [
            ("Gym", self.view_gyms),
            ("Add Gym", self.add_gym),
            ("Appointments", self.view_appointments),
            ("Schedule Appointment", self.schedule_appointment),
            ("Dashboard", self.view_dashboard)
        ]

        for (text, command) in nav_buttons:
            button = tk.Button(self.menu_frame, text=text, font=('Helvetica', 14), bg='red', fg='black',
                               command=command)
            button.pack(fill=tk.X, pady=5)

            # Add the EXIT button at the bottom of the navigation bar
        exit_button = tk.Button(self.menu_frame, text="EXIT", font=('Helvetica', 14), bg='red', fg='black',
                                command=self.exit_application)
        exit_button.pack(side=tk.BOTTOM, pady=10)

    def exit_application(self):
        self.root.quit()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def update_main_frame(self, content):
        self.clear_frame()
        label = tk.Label(self.main_frame, text=content, font=('Helvetica', 20), bg='black', fg='yellow')
        label.pack(pady=20)

    def add_gym(self):
        self.history.append(self.view_gyms)
        self.update_main_frame("Add a New Gym")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Gym ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                  padx=10, pady=5)
        gym_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        gym_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="City:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1, column=0,
                                                                                                padx=10, pady=5)
        city_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        city_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Manager Name:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2, column=0,
                                                                                                        padx=10, pady=5)
        manager_name_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        manager_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Manager Contact:", font=('Helvetica', 14), bg='black', fg='white').grid(row=3,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=5)
        manager_contact_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        manager_contact_entry.grid(row=3, column=1, padx=10, pady=5)

        def submit():
            gym_id = gym_id_entry.get()
            city = city_entry.get()
            manager_name = manager_name_entry.get()
            manager_contact = manager_contact_entry.get()

            if gym_id and city and manager_name and manager_contact:
                manager = self.gym_management.gym_manager(gym_id, manager_name, manager_contact)
                gym = self.gym_management.gym(gym_id, city, manager)
                self.gym_management.add_gym(gym)
                messagebox.showinfo("Success", "Gym added successfully!")
                self.view_gyms()
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=4, columnspan=2, pady=10)

    def view_gyms(self):
        self.history.append(self.update_main_frame)
        self.update_main_frame("View All Gyms")

        gyms = self.gym_management.get_gyms()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for gym in gyms:
            gym_button = tk.Button(list_frame,
                                   text=f"Gym ID: {gym.get_location_id()}, City: {gym.get_city()}, Manager: {gym.get_gym_manager().get_name()}",
                                   font=('Helvetica', 14), bg='yellow', fg='black',
                                   command=lambda g=gym: self.view_gym_detail(g))
            gym_button.pack(pady=5, fill=tk.X)

    def view_gym_detail(self, gym):
        self.history.append(lambda: self.view_gym_detail(gym))
        self.update_main_frame(f"Gym ID: {gym.get_location_id()}, City: {gym.get_city()}")

        tk.Label(self.main_frame, text=f"Manager: {gym.get_gym_manager().get_name()}", font=('Helvetica', 14),
                 bg='black', fg='white').pack(pady=10)

        workout_zone_button = tk.Button(self.main_frame, text="View Workout Zones", font=('Helvetica', 14), bg='yellow',
                                        fg='black', command=lambda: self.view_workout_zones(gym))
        workout_zone_button.pack(pady=5)

        member_button = tk.Button(self.main_frame, text="View Members", font=('Helvetica', 14), bg='yellow',
                                   fg='black', command=lambda: self.view_members(gym))
        member_button.pack(pady=5)

        payment_button = tk.Button(self.main_frame, text="View Payments", font=('Helvetica', 14), bg='yellow',
                                   fg='black', command=lambda: self.view_payments(gym))
        payment_button.pack(pady=5)

        subscription_button = tk.Button(self.main_frame, text="View Subscriptions", font=('Helvetica', 14), bg='yellow',
                                   fg='black', command=lambda: self.view_subscriptions(gym))
        subscription_button.pack(pady=5)

        attendance_button = tk.Button(self.main_frame, text="View Attendance", font=('Helvetica', 14), bg='yellow',
                                        fg='black', command=lambda: self.view_attendance(gym))
        attendance_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=self.view_gyms)
        back_button.pack(side=tk.BOTTOM, pady=10)

        self.saved_gym = gym

    def view_workout_zones(self, gym):
        self.history.append(lambda: self.view_workout_zones(gym))
        self.update_main_frame("View Workout Zones")

        zones = gym.get_workout_zones()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for zone in zones:
            zone_button = tk.Button(list_frame,
                                    text=f"Zone ID: {zone.get_zone_id()}, Exercise Type: {zone.get_exercise_type()}",
                                    font=('Helvetica', 14), bg='yellow', fg='black',
                                    command=lambda z=zone: self.view_workout_zone_detail(z))
            zone_button.pack(pady=5, fill=tk.X)

        add_zone_button = tk.Button(self.main_frame, text="Add Workout Zone", font=('Helvetica', 14), bg='yellow',
                                    fg='black', command=lambda: self.add_workout_zone(gym))
        add_zone_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_gym_detail(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

        self.saved_gym = gym

    def view_workout_zone_detail(self, zone):
        self.history.append(lambda: self.view_workout_zone_detail(zone))
        self.update_main_frame(f"Zone ID: {zone.get_zone_id()}, Exercise Type: {zone.get_exercise_type()}")

        tk.Label(self.main_frame, text=f"Attendant: {zone.get_attendant()}", font=('Helvetica', 14), bg='black',
                 fg='white').pack(pady=10)

        update_button = tk.Button(self.main_frame, text="View Updates", font=('Helvetica', 14), bg='yellow', fg='black',
                                  command=lambda: self.view_updates(zone))
        update_button.pack(pady=5)

        schedule_button = tk.Button(self.main_frame, text="View Schedules", font=('Helvetica', 14), bg='yellow',
                                    fg='black', command=lambda: self.view_schedules(zone))
        schedule_button.pack(pady=5)

        promotion_button = tk.Button(self.main_frame, text="View Promotions", font=('Helvetica', 14), bg='yellow',
                                     fg='black', command=lambda: self.view_promotions(zone))
        promotion_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_workout_zones(self.saved_gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

        self.saved_zone = zone

    def add_workout_zone(self, gym):
        self.history.append(lambda: self.add_workout_zone(gym))
        self.update_main_frame("Add a New Workout Zone")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Zone ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                   padx=10, pady=5)
        zone_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        zone_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Exercise Type:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5)
        exercise_type_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        exercise_type_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Attendant:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2, column=0,
                                                                                                     padx=10, pady=5)
        attendant_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        attendant_entry.grid(row=2, column=1, padx=10, pady=5)

        def submit():
            zone_id = zone_id_entry.get()
            exercise_type = exercise_type_entry.get()
            attendant = attendant_entry.get()

            if zone_id and exercise_type and attendant:
                zone = self.gym_management.workout_zone(zone_id, exercise_type, attendant)
                gym.add_workout_zone(zone)
                messagebox.showinfo("Success", "Workout Zone added successfully!")
                self.view_workout_zones(gym)
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=3, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_workout_zones(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_updates(self, zone):
        self.history.append(lambda: self.view_updates(zone))
        self.update_main_frame("View Updates")

        updates = zone.get_updates()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for update in updates:
            tk.Label(list_frame, text=update, font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        add_update_button = tk.Button(self.main_frame, text="Add Update", font=('Helvetica', 14), bg='yellow',
                                      fg='black', command=lambda: self.add_update(zone))
        add_update_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_workout_zone_detail(zone))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def add_update(self, zone):
        self.history.append(lambda: self.add_update(zone))
        self.update_main_frame("Add Update")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Update:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                  padx=10, pady=5)
        update_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        update_entry.grid(row=0, column=1, padx=10, pady=5)

        def submit():
            update = update_entry.get()
            if update:
                zone.add_update(update)
                messagebox.showinfo("Success", "Update added successfully!")
                self.view_updates(zone)
            else:
                messagebox.showwarning("Error", "Update field is required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=1, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_updates(zone))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_schedules(self, zone):
        self.history.append(lambda: self.view_schedules(zone))
        self.update_main_frame("View Schedules")

        schedules = zone.get_schedules()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for schedule in schedules:
            tk.Label(list_frame, text=schedule, font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        add_schedule_button = tk.Button(self.main_frame, text="Add Schedule", font=('Helvetica', 14), bg='yellow',
                                        fg='black', command=lambda: self.add_schedule(zone))
        add_schedule_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_workout_zone_detail(zone))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def add_schedule(self, zone):
        self.history.append(lambda: self.add_schedule(zone))
        self.update_main_frame("Add Schedule")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Schedule:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                    padx=10, pady=5)
        schedule_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        schedule_entry.grid(row=0, column=1, padx=10, pady=5)

        def submit():
            schedule = schedule_entry.get()
            if schedule:
                zone.add_schedule(schedule)
                messagebox.showinfo("Success", "Schedule added successfully!")
                self.view_schedules(zone)
            else:
                messagebox.showwarning("Error", "Schedule field is required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=1, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_schedules(zone))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_promotions(self, zone):
        self.history.append(lambda: self.view_promotions(zone))
        self.update_main_frame("View Promotions")

        promotions = zone.get_promotions()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for promotion in promotions:
            tk.Label(list_frame, text=promotion, font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        add_promotion_button = tk.Button(self.main_frame, text="Add Promotion", font=('Helvetica', 14), bg='yellow',
                                         fg='black', command=lambda: self.add_promotion(zone))
        add_promotion_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_promotions(zone))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def add_promotion(self, zone):
        self.history.append(lambda: self.add_promotion(zone))
        self.update_main_frame("Add Promotion")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Promotion:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                     padx=10, pady=5)
        promotion_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        promotion_entry.grid(row=0, column=1, padx=10, pady=5)

        def submit():
            promotion = promotion_entry.get()
            if promotion:
                zone.add_promotion(promotion)
                messagebox.showinfo("Success", "Promotion added successfully!")
                self.view_promotions(zone)
            else:
                messagebox.showwarning("Error", "Promotion field is required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=1, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_promotions(zone))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def add_member(self, gym):
        self.history.append(lambda: self.view_members(gym))
        self.update_main_frame("Add a New Member")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Member ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                     padx=10, pady=5)
        member_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        member_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Personal Details:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)
        personal_details_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        personal_details_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Health Information:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=5)
        health_info_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        health_info_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Membership Status:", font=('Helvetica', 14), bg='black', fg='white').grid(row=3,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=5)
        membership_status_combobox = ttk.Combobox(form_frame, values=["Regular", "Premium", "Trial"], font=('Helvetica', 14))
        membership_status_combobox.grid(row=3, column=1, padx=10, pady=5)

        def submit():
            member_id = member_id_entry.get()
            personal_details = personal_details_entry.get()
            health_info = health_info_entry.get()
            membership_status = membership_status_combobox.get()

            if member_id and personal_details and health_info and membership_status:
                member = self.gym_management.member(member_id, personal_details, health_info, membership_status)
                gym.add_member(member)
                messagebox.showinfo("Success", "Member added successfully!")
                self.view_members(gym)
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=4, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_members(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_members(self, gym):
        self.history.append(lambda: self.view_members(gym))
        self.update_main_frame("View All Members")

        members = gym.get_members()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for member in members:
            tk.Label(list_frame,
                     text=f"Member ID: {member.get_member_id()}, Personal Details: {member.get_personal_details()}, Health Info: {member.get_health_info()}, Status: {member.get_membership_status()}",
                     font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        add_member_button = tk.Button(self.main_frame, text="Add Member", font=('Helvetica', 14), bg='yellow',
                                      fg='black', command=lambda: self.add_member(gym))
        add_member_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_gym_detail(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def schedule_appointment(self):
        self.history.append(self.view_appointments)
        self.update_main_frame("Schedule an Appointment")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Appointment ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
        appointment_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        appointment_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Member ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1, column=0,
                                                                                                     padx=10, pady=5)
        member_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        member_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Trainer:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2, column=0,
                                                                                                   padx=10, pady=5)
        trainer_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        trainer_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Appointment Type:", font=('Helvetica', 14), bg='black', fg='white').grid(row=3,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)
        appointment_type_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        appointment_type_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Schedule:", font=('Helvetica', 14), bg='black', fg='white').grid(row=4, column=0,
                                                                                                    padx=10, pady=5)
        schedule_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        schedule_entry.grid(row=4, column=1, padx=10, pady=5)

        def submit():
            appointment_id = appointment_id_entry.get()
            member_id = member_id_entry.get()
            trainer = trainer_entry.get()
            appointment_type = appointment_type_entry.get()
            schedule = schedule_entry.get()

            if appointment_id and member_id and trainer and appointment_type and schedule:
                appointment = self.gym_management.appointment(appointment_id, member_id, trainer,
                                                              appointment_type, schedule)
                if self.gym_management.get_gyms():
                    self.gym_management.get_gyms()[0].add_appointment(appointment)
                    messagebox.showinfo("Success", "Appointment scheduled successfully!")
                else:
                    messagebox.showwarning("Error", "No gyms available to schedule the appointment.")
                self.view_appointments()
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=5, columnspan=2, pady=10)

    def view_appointments(self):
        self.history.append(self.update_main_frame)
        self.update_main_frame("View All Appointments")

        if not self.gym_management.get_gyms():
            messagebox.showwarning("Error", "No gyms available.")
            return

        appointments = self.gym_management.get_gyms()[0].get_appointments()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for appointment in appointments:
            tk.Label(list_frame,
                     text=f"Appointment ID: {appointment.get_appointment_id()}, Member ID: {appointment.get_member()}, Trainer: {appointment.get_trainer()}, Type: {appointment.get_appointment_type()}, Schedule: {appointment.get_schedule()}",
                     font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

    def record_payment(self, gym):
        self.history.append(lambda: self.record_payment(gym))
        self.update_main_frame("Record a Payment")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Payment ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0, column=0,
                                                                                                      padx=10, pady=5)
        payment_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        payment_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Member ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1, column=0,
                                                                                                     padx=10, pady=5)
        member_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        member_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Amount:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2, column=0,
                                                                                                  padx=10, pady=5)
        amount_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        amount_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Payment Method:", font=('Helvetica', 14), bg='black', fg='white').grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
        payment_method_combobox = ttk.Combobox(form_frame, values=["Card", "Cash"], font=('Helvetica', 14))
        payment_method_combobox.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Date:", font=('Helvetica', 14), bg='black', fg='white').grid(row=4, column=0,
                                                                                                padx=10, pady=5)
        date_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        date_entry.grid(row=4, column=1, padx=10, pady=5)

        def submit():
            payment_id = payment_id_entry.get()
            member_id = member_id_entry.get()
            amount = amount_entry.get()
            payment_method = payment_method_combobox.get()
            date = date_entry.get()

            if payment_id and member_id and amount and payment_method and date:
                payment = self.gym_management.payment(payment_id, member_id, amount, payment_method, date)
                gym.add_payment(payment)
                messagebox.showinfo("Success", "Payment recorded successfully!")
                self.view_payments(gym)
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=5, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_payments(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_payments(self, gym):
        self.history.append(lambda: self.view_payments(gym))
        self.update_main_frame("View All Payments")

        payments = gym.get_payments()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for payment in payments:
            tk.Label(list_frame,
                     text=f"Payment ID: {payment.get_payment_id()}, Member ID: {payment.get_member()}, Amount: {payment.get_amount()}, Method: {payment.get_payment_method()}, Date: {payment.get_date()}",
                     font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        record_payment_button = tk.Button(self.main_frame, text="Record Payment", font=('Helvetica', 14), bg='yellow',
                                          fg='black', command=lambda: self.record_payment(gym))
        record_payment_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_gym_detail(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def add_subscription(self, gym):
        self.history.append(lambda: self.view_subscriptions(gym))
        self.update_main_frame("Add a Subscription")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Subscription ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=5)
        subscription_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        subscription_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Member ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1, column=0,
                                                                                                     padx=10, pady=5)
        member_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        member_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Plan Type:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2, column=0,
                                                                                                     padx=10, pady=5)
        plan_type_combobox = ttk.Combobox(form_frame, values=["Monthly", "Quarterly", "Annual"], font=('Helvetica', 14))
        plan_type_combobox.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Start Date:", font=('Helvetica', 14), bg='black', fg='white').grid(row=3, column=0,
                                                                                                      padx=10, pady=5)
        start_date_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        start_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="End Date:", font=('Helvetica', 14), bg='black', fg='white').grid(row=4, column=0,
                                                                                                    padx=10, pady=5)
        end_date_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        end_date_entry.grid(row=4, column=1, padx=10, pady=5)

        def submit():
            subscription_id = subscription_id_entry.get()
            member_id = member_id_entry.get()
            plan_type = plan_type_combobox.get()
            start_date = start_date_entry.get()
            end_date = end_date_entry.get()

            if subscription_id and member_id and plan_type and start_date and end_date:
                subscription = self.gym_management.subscription(subscription_id, member_id, plan_type, start_date,
                                                                end_date)
                gym.add_subscription(subscription)
                messagebox.showinfo("Success", "Subscription added successfully!")
                self.view_subscriptions(gym)
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=5, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_subscriptions(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_subscriptions(self, gym):
        self.history.append(lambda: self.view_subscriptions(gym))
        self.update_main_frame("View All Subscriptions")

        subscriptions = gym.get_subscriptions()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for subscription in subscriptions:
            tk.Label(list_frame,
                     text=f"Subscription ID: {subscription.get_subscription_id()}, Member ID: {subscription.get_member()}, Plan: {subscription.get_plan_type()}, Start Date: {subscription.get_start_date()}, End Date: {subscription.get_end_date()}",
                     font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        add_subscription_button = tk.Button(self.main_frame, text="Add Subscription", font=('Helvetica', 14), bg='yellow',
                                          fg='black', command=lambda: self.add_subscription(gym))
        add_subscription_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_gym_detail(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def record_attendance(self, gym):
        self.history.append(lambda: self.view_attendance(gym))
        self.update_main_frame("Record Attendance")

        form_frame = tk.Frame(self.main_frame, bg='black')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Attendance ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5)
        attendance_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Member ID:", font=('Helvetica', 14), bg='black', fg='white').grid(row=1, column=0,
                                                                                                     padx=10, pady=5)
        member_id_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        member_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Date:", font=('Helvetica', 14), bg='black', fg='white').grid(row=2, column=0,
                                                                                                padx=10, pady=5)
        date_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Activity:", font=('Helvetica', 14), bg='black', fg='white').grid(row=3, column=0,
                                                                                                    padx=10, pady=5)
        activity_entry = tk.Entry(form_frame, font=('Helvetica', 14))
        activity_entry.grid(row=3, column=1, padx=10, pady=5)

        def submit():
            attendance_id = attendance_id_entry.get()
            member_id = member_id_entry.get()
            date = date_entry.get()
            activity = activity_entry.get()

            if attendance_id and member_id and date and activity:
                attendance = self.gym_management.attendance(attendance_id, member_id, date, activity)
                gym.add_attendance(attendance)
                messagebox.showinfo("Success", "Attendance recorded successfully!")
                self.view_attendance(gym)
            else:
                messagebox.showwarning("Error", "All fields are required!")

        tk.Button(form_frame, text="Submit", command=submit, font=('Helvetica', 14), bg='yellow', fg='black').grid(
            row=4, columnspan=2, pady=10)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_attendance(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_attendance(self, gym):
        self.history.append(lambda: self.view_attendance(gym))
        self.update_main_frame("View All Attendance Records")

        attendance_records = gym.get_attendance()

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        for attendance in attendance_records:
            tk.Label(list_frame,
                     text=f"Attendance ID: {attendance.get_attendance_id()}, Member ID: {attendance.get_member()}, Date: {attendance.get_date()}, Activity: {attendance.get_activity()}",
                     font=('Helvetica', 14), bg='black', fg='white').pack(pady=5)

        record_attendance_button = tk.Button(self.main_frame, text="Record Attendance", font=('Helvetica', 14), bg='yellow',
                                          fg='black', command=lambda: self.record_attendance(gym))
        record_attendance_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Back", font=('Helvetica', 14), bg='red', fg='black',
                                command=lambda: self.view_gym_detail(gym))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def view_dashboard(self):
        self.history.append(self.update_main_frame)
        self.update_main_frame("Staff Management Dashboard")

        if not self.gym_management.get_gyms():
            messagebox.showwarning("Error", "No gyms available.")
            return

        list_frame = tk.Frame(self.main_frame, bg='black')
        list_frame.pack(pady=10)

        save_csv_button = tk.Button(list_frame, text="Save CSV Report", font=('Helvetica', 14), bg='yellow', fg='black',
                                    command=self.save_csv_report)
        save_csv_button.pack(pady=5)

        create_chart_button = tk.Button(list_frame, text="Create Bar Chart Report", font=('Helvetica', 14), bg='yellow',
                                        fg='black', command=self.create_bar_chart_report)
        create_chart_button.pack(pady=5)

    def save_csv_report(self):
        gyms = self.gym_management.get_gyms()

        with open('gym_report.csv', 'w', newline='') as csvfile:
            fieldnames = ['GymID', 'Gym Manager', 'Number of Members', 'Total Income']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for gym in gyms:
                writer.writerow({
                    'GymID': gym.get_location_id(),
                    'Gym Manager': gym.get_gym_manager().get_name(),
                    'Number of Members': len(gym.get_members()),
                    'Total Income': sum(payment.get_amount() for payment in gym.get_payments())
                })

        messagebox.showinfo("Success", "CSV report saved successfully!")

    def create_bar_chart_report(self):
        try:
            with open('gym_report.csv', mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV report file not found. Please save the CSV report first.")
            return

        gym_ids = [row['GymID'] for row in data]
        number_of_members = [int(row['Number of Members']) for row in data]
        total_income = [float(row['Total Income']) for row in data]

        x = range(len(gym_ids))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        bars1 = ax.bar([i - width / 2 for i in x], number_of_members, width, label='Number of Members')
        bars2 = ax.bar([i + width / 2 for i in x], total_income, width, label='Total Income')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel('Gym ID')
        ax.set_ylabel('Values')
        ax.set_title('Gym Report')
        ax.set_xticks(x)
        ax.set_xticklabels(gym_ids)
        ax.legend()

        plt.xticks(rotation=45)
        fig.tight_layout()

        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementApp(root)
    root.mainloop()
