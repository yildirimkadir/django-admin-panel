from django.contrib import admin
from .models import Product
from django.utils import timezone
# Register your models here.
# readonly_fields = ("bring_image",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago")
    list_editable = ( "is_in_stock", )
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 15
    date_hierarchy = "update_date"
    
    actions = ("is_in_stock", )

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
    
    def added_days_ago(self, product):
        
        fark = timezone.now() - product.create_date
        return fark.days 

admin.site.register(Product, ProductAdmin)

admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"