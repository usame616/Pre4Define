from django.contrib import admin
from .models import Define


# Register your models here.

class DefineAdmin(admin.ModelAdmin):
    list_display = ['word' , 'category' , 'ranking']
    list_display_links = ['word' , 'category']
    list_filter = ['commentScore' , 'commentCount']
    search_fields = ['word','category']


    class Meta:
        model = Define


admin.site.register(Define , DefineAdmin)
