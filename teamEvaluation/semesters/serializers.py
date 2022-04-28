from rest_framework import serializers

from .models import Semester


class SemesterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Semester
		fields = '__all__'

class UpdateSemesterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Semester
		fields = ['semester', 'year']
