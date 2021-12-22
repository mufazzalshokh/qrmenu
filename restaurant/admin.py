from django.contrib import admin

from restaurant.models import MenuModel, Restaurant, TableModel, CategoryModel, UserModel, OrderModel

admin.site.register(TableModel)
admin.site.register(OrderModel)
admin.site.register(UserModel)
admin.site.register(CategoryModel)
admin.site.register(MenuModel)
admin.site.register(Restaurant)
