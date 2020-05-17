from django.contrib import admin

# from django.contrib.auth.models import Group
from .models import ReferenceBook
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ReferenceBookAdmin(ImportExportModelAdmin):
    list_display = ('id','article_title','article_topic_type','article_updated_by','likes','dislikes','last_updated_date')
    list_editable = ('article_title',)
    list_per_page = 20
    search_fields = ('article_id','article_title')
    list_filter = ('article_updated_by','likes','last_updated_date')

admin.site.register(ReferenceBook, ReferenceBookAdmin)
# admin.site.unregister(Group)


