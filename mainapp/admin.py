from django.contrib import admin

import mainapp.models


# Register your models here.
@admin.register(mainapp.models.SavedData)
class SavedDataAdmin(admin.ModelAdmin):
    list_display = ['username', 'abstract', 'keywords']
