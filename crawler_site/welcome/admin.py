from django.contrib import admin

# from .models import Vendor, Food , VendorAdmin, FoodAdmin   #若要將admin顯示也須將其class引入

# 在model採用decorator就不用每次都要引入了
from .models import Vendor, Food  #若要將admin顯示也須將其class引入
# # Register your models here.
# admin.site.register(Vendor, VendorAdmin)
# admin.site.register(Food, FoodAdmin)


# 在model採用decorator就不用每次都要引入了
# Register your models here.
# admin.site.register(Vendor)
# admin.site.register(Food)