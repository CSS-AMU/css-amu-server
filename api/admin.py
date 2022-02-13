from django.contrib import admin
from .models import Achievement, Event, Publication, Member

# Register your models here.
admin.site.register(Achievement)
admin.site.register(Event)
admin.site.register(Publication)
admin.site.register(Member)
