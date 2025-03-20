from rest_framework import serializers
from .models import Trainee

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id', 'first_name', 'last_name', 'email']