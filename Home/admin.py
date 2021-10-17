from django.contrib import admin

from .models import Contact,Upload_Books,Orders,Seller

# Register your models here.
admin.site.register(Contact)

admin.site.register(Upload_Books)

admin.site.register(Orders)


@admin.register(Seller)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']