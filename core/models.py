from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WebUser(models.Model):
    id = models.CharField(max_length=200, help_text="Test only auth sub claim", primary_key=True)
    name = models.CharField(max_length=200, help_text="Test only auth name claim")
    group = models.TextField(choices=[("Exp", "Exp"), ("Waitlist", "Waitlist")], default="Exp")
    currentDay = models.FloatField(default=1, help_text="User task progress - note that this number might be a float")
    startDate = models.DateField(null=True, blank=True, help_text="Experiment start date")

    banFlag = models.BooleanField(default=False, help_text="This field is managed by automatic rules which cannot be changed by admin")

    freeWriting = models.JSONField(blank=True)
    challengeWriting1 = models.JSONField(blank=True)
    challengeWriting2 = models.JSONField(blank=True)
    challengeWriting3 = models.JSONField(blank=True)
    virtualLetter = models.JSONField(blank=True)
    
    feedback6 = models.JSONField(blank=True)
    feedback8 = models.JSONField(blank=True)
    
    
    def __str__(self):
        return f'{self.sub} | {self.group} | startDate: {self.startDate} | currentDay: {self.currentDay}'

    