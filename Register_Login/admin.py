from Register_Login.models import Profile
from django.contrib import admin
from firebase_admin import messaging
from django.forms import CheckboxSelectMultiple
from django.db import models

# Register your models here.




class profile_admin(admin.ModelAdmin):
    list_filter = ("email","first_name", "last_name", "last_modified")
    list_display = ("email","first_name", 'last_name','last_modified','PhoneNumber','is_active','id'
                  )
    search_fields = ['email']
    formfield_overrides = {
        models.ManyToManyField : {'widget' : CheckboxSelectMultiple},
    }



admin.site.register(Profile, profile_admin)


