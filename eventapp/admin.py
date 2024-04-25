from django.contrib import admin
from .models import Event
from .models import Registration
# username: admin, password: password
# Register your models here.
admin.site.register(Event)
admin.site.register(Registration)