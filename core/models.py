from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WebUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Auth user")
    name = models.CharField(max_length=200, help_text="Test only auth name claim")
    sub = models.CharField(max_length=200, help_text="Test only auth sub claim")
    group = models.TextField(choices=[("Exp", "Exp"), ("Waitlist", "Waitlist")], default="Exp")
    currentDay = models.FloatField(default=1, help_text="User task progress - note that this number might be a float")
    startDate = models.DateField(null=True, blank=True, help_text="Experiment start date")

    banFlag = models.BooleanField(default=False, help_text="This field is managed by automatic rules which cannot be changed by admin")

    feedback4 = models.TextField(null=True, blank=True)
    feedback4Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    feedback5 = models.TextField(null=True, blank=True)
    feedback5Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    feedback6 = models.TextField(null=True, blank=True)
    feedback6Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")
    feedback8 = models.TextField(null=True, blank=True)
    feedback8Viewed = models.BooleanField(default=False, help_text="Auto set to true when user views feedback")

    def __str__(self):
        return f'{self.sub} | {self.group} | startDate: {self.startDate} | currentDay: {self.currentDay}'

    