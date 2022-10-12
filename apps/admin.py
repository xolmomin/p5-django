from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.models import Region, District, Product, Cart, Category, Wishlist

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)


@admin.register(Region)
class Region(ImportExportModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    exclude = ['slug']


@admin.register(District)
class Region(ImportExportModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    # list_filter = ['name']
