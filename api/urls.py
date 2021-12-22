from django.urls import path, include

from api.views import MenuListAPIView, CategoryAPIView, OrderListApiView, \
	OrderModelCreateAPIView

app_name = 'api'

urlpatterns = [
	path('cat/', CategoryAPIView.as_view()),
	path('menu/', MenuListAPIView.as_view()),
	path('list/', OrderListApiView.as_view()),
	path('cart/create/', OrderModelCreateAPIView.as_view()),
]
