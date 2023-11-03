from Register_Login.models import Profile,Team_Member
from django.contrib import admin
from firebase_admin import messaging
from django.forms import CheckboxSelectMultiple
from django.db import models

# Register your models here.




class Register(admin.ModelAdmin):
    list_filter = ("email","first_name", "last_name", "last_modified")
    list_display = ("email","first_name", 'last_name','last_modified','PhoneNumber','is_active','id'
                  )
    search_fields = ['email']
    formfield_overrides = {
        models.ManyToManyField : {'widget' : CheckboxSelectMultiple},
    }



class Team_Admin(admin.ModelAdmin):
    model = Team_Member
    list_display = ('first_name','last_name','email','PhoneNumber')






class Event_Admin(admin.ModelAdmin):
    list_display = ('email', "Organization", 'PhoneNumber','date','created')




admin.site.register(Profile, Register)
admin.site.register(Team_Member, Team_Admin)


