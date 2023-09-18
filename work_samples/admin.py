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


admin.site.register(WorkSampleImage, WorkSampleImageAdmin)


class WorkSampleTagAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


admin.site.register(WorkSampleTag, WorkSampleTagAdmin)


class WorksampleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'tags_list'
    ]
    list_filter = ['tags']
    search_fields = ['title']

    def tags_list(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags


admin.site.register(WorkSample, WorksampleAdmin)
