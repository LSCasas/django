from django.db import models

# Create your models here.

class Koder(models.Model):
    """Koder Model."""

    STATUSES = [
        ("active", "Active"), ("inactive", "Inactive"),
        ("finished", "Finished")
    ]
    SIZES = [
        ("s", "Small"), ("m", "Medium"),
        ("l", "Large")
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    generation = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=8, choices=STATUSES, default="active")
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"