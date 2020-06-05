from django.contrib import admin
from .models import Field, Category

# class PersonAdmin(admin.ModelAdmin):
   

class FieldAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Field Name',		{'fields': ['name']}),
        ('Description',		{'fields': ['description']}),
        ('Category', 		{'fields': ['category.name']}),
    ]



class CategoryAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Name',		{'fields': ['name']}),
        ('Description',	{'fields': ['description']}),
    ]

admin.site.register(Field, FieldAdmin)
admin.site.register(Category, CategoryAdmin)
