from rest_framework import serializers
from . models import Car, ShowRoom


class CarSerializers(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = "__all__"
        # exclude = ['status']

    def get_discounted_price(self, object):
        discountPrice = object.price - 5000
        return discountPrice

    # def validate_price(self, value):
    #     if value <= 20000:    
    #         return serializers.ValidationError('Price mustbe gretter then 2000')
    #     return value


    # id = serializers.IntegerField(read_only = True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # status = serializers.BooleanField(read_only = True)

    # def create(self, validated_data):
    #     # return super().create(validated_data)
    #     return Car.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance


class ShowRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = "__all__"