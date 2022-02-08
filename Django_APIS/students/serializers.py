from rest_framework import serializers
from students.models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class IntakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intake
        fields = '__all__'


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
