from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Vous pouvez personnaliser l'affichage ou l'édition des champs ici si nécessaire
    pass