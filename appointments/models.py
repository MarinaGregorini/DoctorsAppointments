from django.db import models
from datetime import time
from website.forms import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    room_number = models.IntegerField()

    def __str__(self):
        return f"Dr. {self.name}"

class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.specialty} appointment with {self.doctor} at {self.start_time} on {self.date}."

class PastAppointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    doctor_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Completed Appointment with {self.doctor_name} at {self.start_time} on {self.date}."