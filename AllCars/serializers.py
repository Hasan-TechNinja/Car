from rest_framework import serializers
from . models import Car


class CarSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField(read_only = True)

    def create(self, validated_data):
        # return super().create(validated_data)
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance