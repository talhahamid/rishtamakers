from django.contrib import admin
from .models import Users,Religion,Religion_category,Status,Education,Occupation,Mothertongue

# Register your models here.
admin.site.register(Users)
admin.site.register(Religion)
admin.site.register(Religion_category)
admin.site.register(Status)
admin.site.register(Education)
admin.site.register(Occupation)
admin.site.register(Mothertongue)