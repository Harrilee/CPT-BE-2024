from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WebUser, Whitelist

@receiver(post_save, sender=WebUser)
def update_whitelist_on_webuser_change(sender, instance, created, **kwargs):
    if not created:
        try:
            whitelist_instance = Whitelist.objects.get(uuid=instance.uuid)
            if whitelist_instance.group != instance.group:
                whitelist_instance.group = instance.group
                whitelist_instance.save()
                
            if whitelist_instance.startDate != instance.startDate:
                whitelist_instance.startDate = instance.startDate
                whitelist_instance.save()
                
        except Whitelist.DoesNotExist:
            pass

@receiver(post_save, sender=Whitelist)
def update_webuser_on_whitelist_change(sender, instance, created, **kwargs):
    if not created:
        try:
            webuser_instance = WebUser.objects.get(uuid=instance.uuid)
            if webuser_instance.group != instance.group:
                webuser_instance.group = instance.group
                webuser_instance.save()
                
            if webuser_instance.startDate != instance.startDate:
                webuser_instance.startDate = instance.startDate
                webuser_instance.save()
                
        except WebUser.DoesNotExist:
            pass
