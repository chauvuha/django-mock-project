from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,  PermissionsMixin

# Create your models here.

# class User(AbstractUser):
#     is_student = models.BooleanField()
#     is_teacher = models.BooleanField()

#     def __str__(self):
#         return self.username

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    # autonow is automatically going to update the time when we save the note
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add only takes the first time when we create
    created = models.DateTimeField(auto_now_add=True)

    # a string representation of the class, it will just be the body attribute.
    def __str__(self):
        return self.body[0:50]

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     # Add your custom fields here
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150)

#     # Set the field that will be used as the username field
#     USERNAME_FIELD = 'email'

#     # Add any additional required fields
#     REQUIRED_FIELDS = ['username']