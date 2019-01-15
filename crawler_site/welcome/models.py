from django.db import models
from django.contrib import admin   #管理admin用

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length = 20)
    store_name = models.CharField(max_length = 10)
    phone_number = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)

    # 覆寫 __str__ ， 它會去改變資料所要顯示的值 (是指例如用django shell取資料的呈現，不是admin頁)
    def __str__(self):
        return self.vendor_name

class Food(models.Model):
    food_name = models.CharField(max_length = 30)
    price_name = models.DecimalField(max_digits = 3, decimal_places=0)
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)    #  當對應到model移除時一倂刪除

    def __str__(self):
        return self.food_name


# 加此管理admin才會顯示id (key直)list_display 是固定寫法，且另外還要另外去admin import才會顯示
# 或者使用decorator
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    # list_display = ('id', 'vendor_name')     # list_display 可以秀全部!ex,
    list_display = [field.name for field in Vendor._meta.fields]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    # list_display = ('id', 'food_name')
    list_display = [field.name for field in Food._meta.fields]
    # 可增加過濾器 list_filter: (最後要有',') , 如此才能在admin進行過濾搜尋，
    # 若想自行開發客制filter: 參考: https://ithelp.ithome.com.tw/articles/10200944
    list_filter = ('price_name',)
    fields = ['price_name']    # fields表示該欄位才可以修改，而fields代表包含，exclude代表除外
    search_fields = ['food_name', 'price_name']   #
    ordering = ['-price_name']

