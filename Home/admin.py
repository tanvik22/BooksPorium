from django.contrib import admin

from .models import Contact,Upload_Books,Orders

# Register your models here.
admin.site.register(Contact)

admin.site.register(Upload_Books)

admin.site.register(Orders)