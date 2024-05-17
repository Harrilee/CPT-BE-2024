from rest_framework import serializers
from .models import WebUser

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUser
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'context' in kwargs and kwargs['context'].get('info'):
            info_fields = [
                'group', 'currentDay', 'startDate', 'banFlag',
                'feedback4', 'feedback4Viewed', 'feedback5', 'feedback5Viewed',
                'feedback6', 'feedback6Viewed', 'feedback8', 'feedback8Viewed' 
            ]
            for field in set(self.fields) - set(info_fields):
                self.fields.pop(field)
            for field in self.fields:
                if field not in ['feedback4Viewed', 'feedback5Viewed', 'feedback6Viewed', 'feedback8Viewed']:
                    self.fields[field].read_only = True
            