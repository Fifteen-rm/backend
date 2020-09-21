from django.db import models
from ..hospital.models import Hospital, Major
import datetime
# Create your models here.

class Doctor(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=10, default='default')
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL)
    contact = models.CharField(max_length=20, default='010-0000-0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "doctor"
        ordering = ['created_at']