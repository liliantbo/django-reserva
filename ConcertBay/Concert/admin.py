from django.contrib import admin

# Register your models here.
from .models import Concierto, Localidad, Ticket

admin.site.register(Concierto)
admin.site.register(Ticket)
admin.site.register(Localidad)
