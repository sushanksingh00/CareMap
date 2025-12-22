from django.db import models
from django.contrib.auth.models import User


class DiagnosisHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diagnoses')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.age}) @ {self.timestamp}"


class UserProfile(models.Model):
    """Extended user details without replacing Django's built-in User.

    Fields requested: name, age, email, phone number, address (city, country), profile photo.
    We store a profile photo URL to avoid file storage setup. This can be
    changed to an ImageField later if local uploads are needed.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=128, blank=True)
    profile_photo_url = models.URLField(blank=True, help_text="Public URL to the profile photo")

    def __str__(self):
        base = self.name or self.user.get_username()
        return f"Profile<{base}>"
