from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_display = ('name', 'character_class', 'level', 'race', 'alignment')
    search_fields = ('name',)
    # search_fields = ('name', 'character_class', 'race', 'alignment')