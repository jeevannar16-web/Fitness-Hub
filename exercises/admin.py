from django.contrib import admin
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'muscle_group', 'difficulty', 'created_at']
    list_filter = ['muscle_group', 'difficulty']
    search_fields = ['name', 'description']
