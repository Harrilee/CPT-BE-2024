from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class WebUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Auth user")
    bludId = models.CharField(null=True, blank=True, max_length=200, help_text="Blued uid")
    sms = models.CharField(null=True, blank=True, default=0, max_length=20)
    phoneNumber = models.CharField(max_length=200, help_text="Encrypted phone number")

    group = models.TextField(choices=[("Exp", "Exp"), ("Waitlist", "Waitlist")], default="Exp")
    currentDay = models.FloatField(default=1, help_text="User task progress - note that this number might be a float")
    startDate = models.DateField(default=timezone.now, help_text="Experiment start date")

    banFlag = models.BooleanField(default=False, help_text="This field is managed by automatic rules which cannot be changed by admin")
    banReason = models.TextField(max_length=200, null=True, blank=True, help_text="Reason for banning user, visible to user")

    freeWriting = models.JSONField(default=dict, null=True, blank=True)
    challengeWriting1 = models.JSONField(default=dict, null=True, blank=True)
    challengeWriting1Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    
    challengeWriting2 = models.JSONField(default=dict, null=True, blank=True)
    challengeWriting2Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    
    challengeWriting3 = models.JSONField(default=dict, null=True, blank=True)
    feedback6 = models.TextField(null=True, blank=True, help_text="Please write feedback in Markdown format")
    feedback6Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    
    virtualLetter = models.JSONField(default=dict, null=True, blank=True)
    feedback8 = models.TextField(null=True, blank=True, help_text="Please write feedback in Markdown format")
    feedback8Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    
    
    game = models.BinaryField(null=True)
    gameBreakFlag = models.BooleanField(default=False)
    gameFinished = models.BooleanField(default=False)
    gameData = models.JSONField(default=dict,null=True, blank=True)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.id} | {self.group} | startDate: {self.startDate} | currentDay: {self.currentDay}'

    def reset_game(self): 
        self.game = None
        self.gameBreakFlag = False
        self.gameFinished = False
        self.gameData = {}
        self.score = 0
        self.save()
        

class Whitelist(models.Model):
    
    phoneNumber = models.CharField(max_length=200, unique=True, help_text="Encypted phone number")

    def __str__(self):
        return self.phoneNumber