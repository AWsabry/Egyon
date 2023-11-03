from rest_framework import serializers
from categories_and_products.models import Vendor,Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.Category_name')
    restaurant_name = serializers.CharField(source='Vendor.Name')
    image = serializers.CharField(source='category.image')
    
    class Meta:
        model = Product
        fields = '__all__'






class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
