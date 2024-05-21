from rest_framework import serializers
from .models import WebUser

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUser
        fields = '__all__'
        
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'context' in kwargs:
            if kwargs['context'].get('info'):
                info_fields = [
                    'group', 'currentDay', 'startDate', 'banFlag',
                ]
                for field in set(self.fields) - set(info_fields):
                    self.fields.pop(field)

            if kwargs['context'].get('writing'):
                writing_field = getattr(user, kwargs['feild_name'], None)

                for field in set(self.fields) - set(writing_field):
                    self.fields.pop(field)
                    