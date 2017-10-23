from rest_framework import serializers
from challenge.models import FoodEntry, Serving, FoodCategory, FoodDetailCategory, DirectionalStatement
from rest_framework import viewsets


class FoodDetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDetailCategory
        fields = '__all__'


class FoodCategorySerializer(serializers.ModelSerializer):
    # food_category_id = FoodDetailCategorySerializer(read_only=True)
    class Meta:
        model = FoodCategory
        # fields = ('_id', 'food_category_short_name', 'food_category_long_name')
        fields = '__all__'

class ServingSerializer(serializers.ModelSerializer):
    food_category_id = FoodCategorySerializer(read_only=True)
    class Meta:
        model = Serving
        fields = '__all__'

class FoodEntrySerializer(serializers.ModelSerializer):
    # food_category_id = ServingSerializer(many=True, read_only=True)

    class Meta:
        model = FoodEntry
        fields = '__all__'





class DirectionalStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionalStatement
        fields = '__all__'

#
# class ViewSet(viewsets.ModelViewSet):
