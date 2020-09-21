from django.db import models
import datetime
# Create your models here.

class Hospital(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30, default='한림성심병원(default)')
    address = models.CharField(max_length=40, default='한림대학길 1')
    contact = models.CharField(max_length=20, default='010-0000-0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "hospitals"
        ordering = ['created_at']

class Major(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30, default='전공 없음')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Doctor's Majors"
        ordering = ['created_at']