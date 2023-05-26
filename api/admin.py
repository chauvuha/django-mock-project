from django.contrib import admin

# Register your models here.
from .models import Note
# from .models import Note, User, Student

# admin.site.register(User)
admin.site.register(Note)
# admin.site.register(Student)