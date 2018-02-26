from django.contrib import admin

from .models import Category, Item


class MyModelAdmin(admin.ModelAdmin):
    exclude = ['deleted_at']


class MyTabularInline(admin.TabularInline):
    exclude = ['deleted_at']


class ItemInline(MyTabularInline):
    fields = ['name']
    model = Item
    extra = 5


class CategoryAdmin(MyModelAdmin):
    fields = ['name']
    inlines = [ItemInline]


admin.site.register(Category, CategoryAdmin)
