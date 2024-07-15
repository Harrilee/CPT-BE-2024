from django.contrib import admin
from .models import WebUser
# Register your models here.


@admin.action(description='Reset game')
def reset_game(modeladmin, request, queryset):
    for obj in queryset:
        obj.reset_game()
        
class WebUserAdmin(admin.ModelAdmin):
    actions = [reset_game]
    
admin.site.register(WebUser, WebUserAdmin)