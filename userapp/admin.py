from django.contrib import admin

# Register your models here.
from .models import Regidb
admin.site.register(Regidb)
from .models import Contactdb
admin.site.register(Contactdb)
from .models import Messagedb
admin.site.register(Messagedb)
