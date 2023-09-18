from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
# Register your models here.


class WorkSampleImageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'display_picture_preview'
    ]

    def display_picture_preview(self, obj):
        return mark_safe(
            f'<img style="max-width: 150px; max-height:150px" src="/media/{obj.picture}" />'
        )


class WorkSampleTagAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


class WorksampleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    list_filter = ['tags']
    search_fields = ['title']


admin.site.register(WorkSampleImage, WorkSampleImageAdmin)
admin.site.register(WorkSample, WorksampleAdmin)
admin.site.register(WorkSampleTag, WorkSampleTagAdmin)
