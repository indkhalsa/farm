from django.contrib import admin
from assist.models import Item, Good , ItemDetail, GoodDetail


class ItemAdmin(admin.ModelAdmin):
    fields = ['Item']
    list_display = ('item')

class GoodAdmin(admin.ModelAdmin):
    fields = ['Good']
    list_display = ('good')

admin.site.register(Item)
admin.site.register(Good)
admin.site.register(ItemDetail)
admin.site.register(GoodDetail)
# Register your models here.
