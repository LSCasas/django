from django.db import models

# Create your models here.

class Appointment(models.Model):
    """Appointment Model."""

    title = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} "
    



class Psychologist(models.Model):
    """Psychologist Model."""

    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    appointment = models.ForeignKey(Appointment, models.PROTECT, related_name="psychologists")
    
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"


class Patient(models.Model):
    """Patient Model."""

    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    biography = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


    appointment = models.ForeignKey(Appointment, models.PROTECT, related_name="patients")
    
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"
    