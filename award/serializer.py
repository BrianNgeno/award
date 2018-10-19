from rest_framework import serializers
from .models import Profile

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'rate')