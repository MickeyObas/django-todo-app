from django.contrib import admin
from .models import User, Task

class AnotherAdminArea(admin.AdminSite):
    site_header = "Custom Admin"

class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Section 1', {
            'fields':('title', 'completed',),
            'description': 'Some text'
        }),
        ('Section 2', {
            'fields':('user', 'body',)
        }),
    )
    list_display = ['title', 'completed', 'created']

# Register your models here.
admin.site.register(Task, TaskAdmin)
