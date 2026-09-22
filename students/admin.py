from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'course',
                    'registration_date', 'is_active')
    list_filter = ('course', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('course',)
    fieldsets = (
        ('STUDENT INFORMATION', {'fields':('first_name', 'last_name','email', 'course')}),
        ('STUDENT STATUS', {'fields':('is_active',)})
    )

admin.site.register(Student, StudentAdmin)
