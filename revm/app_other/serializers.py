from rest_framework import serializers

from .models import OtherRequest, OtherOffer, Category, Subcategory


class OtherCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OtherSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class OtherOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherOffer
        fields = "__all__"


class OtherRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherRequest
        fields = "__all__"
