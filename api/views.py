from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView

from api.serializers import MenuModelSerializer, CategoryModelSerializer, OrderModelSerializer
from restaurant.models import MenuModel, CategoryModel, OrderModel


class CategoryAPIView(ListAPIView):
	queryset = CategoryModel.objects.all()
	serializer_class = CategoryModelSerializer


class MenuListAPIView(ListAPIView):
	queryset = MenuModel.objects.all()
	serializer_class = MenuModelSerializer


class OrderModelCreateAPIView(CreateAPIView):
	queryset = OrderModel.objects.all()
	serializer_class = OrderModelSerializer


# def create(self, request, *args, **kwargs):
# 	products = json.loads(self.request.POST.get('products'))
# 	totalPrice = 0
# 	numberofproducts = 0
# 	title = 0
#
# 	for i in products[0]['products']:


class OrderListApiView(ListAPIView):
	queryset = OrderModel.objects.all()
	serializer_class = OrderModelSerializer
