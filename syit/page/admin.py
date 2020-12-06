from django.contrib import admin
from .models import life, work, lines
# Register your models here.

class lifeAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'tag', 'heading', 'date',)
    fields = ['file_name', 'tag', 'page_text']

class workAdmin(admin.ModelAdmin):
    list_display = ('name_file', )

class linesAdmin(admin.ModelAdmin):
    list_display = ('years', 'id')

admin.site.register(life, lifeAdmin)
admin.site.register(work, workAdmin)
admin.site.register(lines, linesAdmin)