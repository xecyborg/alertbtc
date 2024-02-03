from django.db import models
from django.conf import settings


class Alert(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('deleted', 'Deleted'),
        ('triggered', 'Triggered'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)