from django.db import models
from doctor.models import Doctor
from patient.models import Patient
from hospital.models import Major
import datetime
# Create your models here.

class Description(models.Model):
    objects = models.Manager()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_say = models.TextField(default='')
    doctor_say = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr {self.doctor} to {self.patient}"
    class Meta:
        verbose_name_plural = "description"
        ordering = ['created_at']

class WaitingRoom(models.Model):
    objects = models.Manager()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"patient {self.patient} ready"
    class Meta:
        verbose_name_plural = "waitingroom"
        ordering = ['created_at']