from django.contrib import admin

from .models import Order, Product

admin.site.site_header = "SupriLinker Dashboard"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "category"]
    list_filter = ["category"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

# admin.site.unregister(Group)
# ^^^^^^^^ UNregister the Group model from the admin site
# ! This is done because we are not using the Group model in this project
