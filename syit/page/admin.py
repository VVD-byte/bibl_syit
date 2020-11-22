from django.contrib import admin
from .models import life
# Register your models here.

class lifeAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'tag', 'heading', 'date',)
    fields = ['file_name', 'tag', 'page_text']

admin.site.register(life, lifeAdmin)