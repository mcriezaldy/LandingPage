from rest_framework import serializers
from .models import Survey

class SurveySubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'name',
            'email',
            'age',
            'satisfaction',
            'feedback',
            'agree_law',
            'agree_parent',
            'agree_ethics',
            'mac_address',
            'ip_address',
            'ap_ip',
        ]