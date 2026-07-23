from django.contrib import admin
from .models import InspirationPost


@admin.register(InspirationPost)
class InspirationPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'quote', 'author']
