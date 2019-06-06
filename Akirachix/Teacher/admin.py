from django.contrib import admin
from .models import Teachers
class TeachersAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email","profession")
	search_fields=("registration_number","email","last_name")
	list_filter=("DateJoined","email")

admin.site.register(Teachers,TeachersAdmin)


# Register your models here.
