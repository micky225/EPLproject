from django.contrib import admin
from .models import Header
from .models import Table,Players,Statistics
# Register your models here.

admin.site.register(Header)
admin.site.register(Table)
admin.site.register(Players)
admin.site.register(Statistics)

