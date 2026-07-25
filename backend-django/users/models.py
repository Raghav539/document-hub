from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """Extended user model with storage quota"""

    email = models.EmailField(unique=True)
    storage_quota = models.BigIntegerField(default=5*1024**3)  # 5GB default
    storage_used = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def __str__(self):
        return self.email

    @property
    def storage_percentage(self):
        """Calculate storage usage percentage"""
        if self.storage_quota == 0:
            return 0
        return (self.storage_used / self.storage_quota) * 100
