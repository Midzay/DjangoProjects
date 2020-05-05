from rest_framework import serializers
from .models import SettingsForRequest

class SettingsSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = SettingsForRequest
        fields = '__all__'
