from django.contrib import admin
from .models import Thread, Profile, Channel

# Register your models here.

admin.site.register(Thread)
admin.site.register(Profile)
admin.site.register(Channel)
