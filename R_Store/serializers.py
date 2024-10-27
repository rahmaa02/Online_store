from rest_framework import serializers
from R_Store import models

class User(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class Order(serializers.ModelSerializer):
    user = User(read_only=True)
    user_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = models.Order
        fields = '__all__'

class Category(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class Product(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'

class Review(serializers.ModelSerializer):
    user = User(read_only=True)
    user_id = serializers.IntegerField(required=False, allow_null=True)
    product = Product(read_only=True)
    product_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = models.Review
        fields = '__all__'