from .models import Category, drugItem
from rest_framework import serializers

# creating category serializers
class CategorySerilizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


# creating drug items serilizers
class drugItemSerilizers(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only = True)
    category = CategorySerilizers(read_only = True)
    class Meta:
        model = drugItem
        fields = ["id", "name", "price", "inStock", "category", "category_id"]