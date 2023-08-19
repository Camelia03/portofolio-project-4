from django.contrib import admin
from .models import Thread, Profile, Channel

# Register your models here.

admin.site.register(Thread)
admin.site.register(Profile)

# Calculate slug for a channel using the name field in the Admin


class ChannelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Channel, ChannelAdmin)
