from django.contrib import admin
from admissions.models import Student


# Register your models here.

class StudentDisplay(admin.ModelAdmin):  # This  is the admin class to display the data as table form in the django
    # admin site
    list_display = ['id', 'name', 'fathername', 'classname', 'contact']


admin.site.register(Student, StudentDisplay)  # StudentDisplay class is the admin class created above to register with
# django admin. it is not mandatory
