from django.contrib import admin
from Home.models import Category, Product, Maker


class TitlePrepopulated(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.
admin.site.register(Category, TitlePrepopulated)
admin.site.register(Product, TitlePrepopulated)
admin.site.register(Maker, TitlePrepopulated)
