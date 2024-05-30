from rest_framework import serializers
from .models import WebUser

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUser
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'context' in kwargs:
            if kwargs['context'].get('info'):
                info_fields = [
                    'group', 'currentDay', 'startDate', 'banFlag',
                ]
                for field in set(self.fields) - set(info_fields):
                    self.fields.pop(field)

            if kwargs['context'].get('writing'):
                for field in set(self.fields) - set([kwargs['context']['field_name']]):
                    self.fields.pop(field)
            