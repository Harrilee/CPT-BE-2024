from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class WebUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Auth user")
    bluedUuid = models.CharField(null=True, blank=True, max_length=200, help_text="Blued uuid")
    sms = models.CharField(null=True, blank=True, default=0, max_length=20)
    phoneNumber = models.CharField(max_length=200, help_text="Encrypted phone number")

    group = models.TextField(choices=[("Exp", "Exp"), ("Waitlist", "Waitlist")], default="Exp")
    currentDay = models.FloatField(default=1, help_text="User task progress - note that this number might be a float")
    startDate = models.DateField(default=timezone.now, help_text="Experiment start date")

    banFlag = models.BooleanField(default=False, help_text="This field is managed by automatic rules which cannot be changed by admin")
    banReason = models.TextField(max_length=200, null=True, blank=True, help_text="Reason for banning user, visible to user")
    banReasonInternal = models.TextField(max_length=500, null=True, blank=True, help_text="Reason for banning user, auto generated")

    freeWriting = models.JSONField(default=dict, null=True, blank=True)
    writingDay1QualityCheck = models.TextField(choices=[("True", "True"), ("False", "False"), ("Null", "Null")], default="Null", help_text="Quality Check for day 1 free writing")
    
    challengeWriting1 = models.JSONField(default=dict, null=True, blank=True)
    challengeWriting1Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    writingDay4QualityCheck = models.TextField(choices=[("True", "True"), ("False", "False"), ("Null", "Null")], default="Null", help_text="Quality Check for day 4 challenge writing")
    
    challengeWriting2 = models.JSONField(default=dict, null=True, blank=True)
    challengeWriting2Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    writingDay5QualityCheck = models.TextField(choices=[("True", "True"), ("False", "False"), ("Null", "Null")], default="Null", help_text="Quality Check for day 5 challenge writing")
    
    challengeWriting3 = models.JSONField(default=dict, null=True, blank=True)
    writingDay6QualityCheck = models.TextField(choices=[("True", "True"), ("False", "False"), ("Null", "Null")], default="Null", help_text="Quality Check for day 6 challenge writing")
    
    feedback6 = models.TextField(null=True, blank=True, help_text="Please write feedback in Markdown format")
    feedback6Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    
    virtualLetter = models.JSONField(default=dict, null=True, blank=True)
    writingDay8QualityCheck = models.TextField(choices=[("True", "True"), ("False", "False"), ("Null", "Null")], default="Null", help_text="Quality Check for day 8 virtual letter")
    
    feedback8 = models.TextField(null=True, blank=True, help_text="Please write feedback in Markdown format")
    feedback8Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    
    game = models.BinaryField(null=True)
    gameBreakFlag = models.BooleanField(default=False)
    gameFinished = models.BooleanField(default=False)
    gameData = models.JSONField(default=dict,null=True, blank=True)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.phoneNumber} | {self.group} | startDate: {self.startDate} | currentDay: {self.currentDay}'

    def reset_game(self): 
        self.game = None
        self.gameBreakFlag = False
        self.gameFinished = False
        self.gameData = {}
        self.score = 0
        self.save()
        
    #TODO
    def validity_check(self):
        banReasons = []
        
        if self.group == "Exp":
            # Criteria 3: Overdue
            if self.currentDay <= 9:
                startDate = datetime.combine(self.startDate, datetime.min.time())
                currenrtTaskStartDate = startDate + timedelta(days=self.currentDay - 1)  # minimum date to start current task
                currentTaskEndDate = currenrtTaskStartDate + timedelta(days=2) + timedelta(hours=4)  # maximum date to finish current task
                print("Checking overdue", currenrtTaskStartDate, currentTaskEndDate)
                if datetime.now() > currentTaskEndDate:
                    banReasons.append("连续2天未完成新任务")
            # Criteria 4: Game
            if self.gameFinished and self.score < 61200:
                    banReasons.append("游戏得分不足61200 (60%)")
        # Criteria 5: Manual ban
        if self.banReason is not None and self.banReason != "":
            banReasons.append("手动标记为不合格")
            
        if len(banReasons) > 0:
            self.banReasonInternal = '；'.join(banReasons) + f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]'
            self.banFlag = True
        else:
            self.banReasonInternal = ''
            self.banFlag = False

        self.save()
        return banReasons

class Whitelist(models.Model):
    
    phoneNumber = models.CharField(max_length=200, unique=True, help_text="Encypted phone number")
    has_add_wechat = models.BooleanField(default=False, help_text="Please set it to true after adding user's wechat")
    
    def __str__(self):
        return self.phoneNumber
    
    
class Log(models.Model):
    
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(WebUser, on_delete=models.CASCADE, null=True, blank=True)
    log = models.TextField()

    def __str__(self) -> str:
        return f'Log [{self.id}] | {self.time.strftime("%Y-%m-%d %H:%M")} | {self.log}'