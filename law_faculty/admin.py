from django.contrib import admin
from .models import Department, Program, Teacher, Specialty, ExchangeProgram

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(Specialty)

@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university', 'languages', 'slots', 'deadline')