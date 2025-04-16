from django.contrib import admin
from .models import Section

class SectionAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Section, SectionAdmin)
