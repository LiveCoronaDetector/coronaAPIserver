from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    confirmator = serializers.IntegerField()
    dead = serializers.IntegerField()
    modifiedDate = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Data.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.confirmator = validated_data.get('confirmator', instance.confirmator)
        instance.dead = validated_data.get('dead', instance.dead)
        instance.modifiedDate = validated_data.get('modifiedDate', instance.modifiedDate)
        instance.save()
        return instance