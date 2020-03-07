from rest_framework import serializers
from .models import Pharmacy

class PharmacySerializer(serializers.Serializer):
    pharmacy_name = serializers.CharField(max_length=50)
    pharmacy_address = serializers.CharField(max_length=80)
    mask = serializers.IntegerField()
    hand_sanitizer = serializers.IntegerField()
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    modifiedDate = serializers.DateTimeField()
    phone = serializers.CharField()

    def create(self, validated_data):
        return Pharmacy.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.pharmacy_name = validated_data.get('pharmacy_name', instance.pharmacy_name)
        instance.pharmacy_address = validated_data.get('pharmacy_address', instance.pharmacy_address)
        instance.mask = validated_data.get('mask', instance.confirmator)
        instance.hand_sanitizer = validated_data.get('hand_sanitizer', instance.hand_sanitizer)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)
        instance.modifiedDate = validated_data.get('modifiedDate', instance.modifiedDate)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
