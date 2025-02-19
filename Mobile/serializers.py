from rest_framework import serializers
from . models import Mobile, Brand


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class MobileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = "__all__"