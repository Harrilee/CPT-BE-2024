from django.contrib import admin
from .models import WebUser, Whitelist, Log
# Register your models here.


@admin.action(description='Reset game')
def reset_game(modeladmin, request, queryset):
    for obj in queryset:
        obj.reset_game()
        
class WebUserAdmin(admin.ModelAdmin):
    actions = [reset_game]
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.validity_check()
    
class WhitelistAdmin(admin.ModelAdmin):
    list_display = ('phoneNumber',)
    

admin.site.register(WebUser, WebUserAdmin)
admin.site.register(Whitelist, WhitelistAdmin)
admin.site.register(Log)