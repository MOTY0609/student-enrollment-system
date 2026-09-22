from django.db import models
from django.conf import settings
# Create your models here.


class Student(models.Model):
    COURSE_CHOICES = [
        ("CS", "Computer Science"),
        ("EE", "Electrical Engineering"),
        ("BA", "Business Administration"),
        ("MED", "Medicine"),
        ("LAW", "Law")
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='students',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
