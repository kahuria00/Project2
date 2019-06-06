from django.contrib import admin
from .models import Students

class StudentsAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email","DateJoined")
	search_fields=("registration_number","email","last_name")
	list_filter=("DateJoined","date_of_birth")
admin.site.register(Students,StudentsAdmin)


# Register your models here.
