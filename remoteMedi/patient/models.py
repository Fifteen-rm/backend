from django.db import models
import datetime
# Create your models here.

class Patient(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=10, default='default')
    contact = models.CharField(max_length=20, default='010-0000-0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "patient"
        ordering = ['created_at']