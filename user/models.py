from django.db import models
from django.contrib.auth.models import AbstractUser

class UserCustomer(AbstractUser):
    nom = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    rôle = models.CharField(max_length=20, default="user")
    préférences = models.JSONField(default=dict, blank=True)
    is_verified = models.BooleanField(default=False)

    # Add unique related_name to avoid clashes with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_customer_groups",  # Unique related_name
        related_query_name="user_customer",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_customer_permissions",  # Unique related_name
        related_query_name="user_customer",
    )

    def _str_(self):
        return self.email