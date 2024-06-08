from django.contrib import admin
from django.apps import apps
from .models import User,Train,Rform

admin.site.register(User)
admin.site.register(Train)
admin.site.register(Rform)



# Register your models here.
