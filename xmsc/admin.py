from django.contrib import admin
from xmsc.models import Phone, Category

# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, PhoneAdmin)
admin.site.register(Category, CategoryAdmin)
