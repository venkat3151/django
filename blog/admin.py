from django.contrib import admin
from .models import Post
from mediumeditor.admin import MediumEditorAdmin


#Register your models here.
@admin.register(Post)
class MyModelAdmin(MediumEditorAdmin, admin.ModelAdmin):
    mediumeditor_fields = ('text', )
