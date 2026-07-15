from django.contrib import admin
from .models import Club, OpeningHours


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass


@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    pass
