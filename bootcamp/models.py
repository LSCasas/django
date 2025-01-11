from django.db import models

# Create your models here.
class Bootcamp(models.Model):
    """Bootcamp Model."""
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} "

class Generation(models.Model):
    """Generation Model."""
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    
    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")
    
    def __str__(self):
        return f"{self.number} {self.bootcamp.name}"


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

    generation = models.ForeignKey(Generation, models.PROTECT, related_name="koders")
    
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"
    

class Mentor(models.Model):
    """Mentor Model."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    

    generations = models.ManyToManyField(Generation, related_name="mentors")

    def __str__(self):
        return f"id -> {self.pk}  {self.first_name} {self.last_name}"


