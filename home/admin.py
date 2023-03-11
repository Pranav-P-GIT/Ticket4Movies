from django.contrib import admin
from .models import Film,Seat

# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ("name","img","star","date","language","duration","genre","dimensional","time")


class SeatAdmin(admin.ModelAdmin):
    list_display = ("total","available","price")



admin.site.register(Film , FilmAdmin)
admin.site.register(Seat , SeatAdmin)
