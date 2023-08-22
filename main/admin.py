from django.contrib import admin
from .models import Image , Landmark


class LandmarkAdminTabularInline(admin.TabularInline):
    model = Landmark

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
    ]
    search_fields = ['name']
    inlines = [LandmarkAdminTabularInline]
