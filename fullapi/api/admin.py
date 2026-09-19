from django.contrib import admin
from .models import Profile,State,City

# Register your models here.
admin.site.register(State)
admin.site.register(City)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name']

