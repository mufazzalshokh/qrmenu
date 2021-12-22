from rest_framework import serializers
from restaurant.models import MenuModel, CategoryModel, TableModel, Restaurant, OrderModel


class CategoryModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = '__all__'


class RestaurantModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name']


class MenuModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuModel
		fields = '__all__'


# fields = ['image', 'name', 'real_price', 'description', 'category']


class TableModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TableModel
		fields = '__all__'


class OrderModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderModel
		fields = '__all__'
