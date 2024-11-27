from rest_framework import serializers
from .models import Task4Murat

class Task4Serializer(serializers.ModelSerializer):
	class Meta:
		model = Task4Murat
		fields ='__all__'