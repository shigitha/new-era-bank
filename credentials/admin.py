from django.contrib import admin

# Register your models here.
from django.forms import ModelForm
from django.contrib import admin
from . models import District,Registration,Branch,Account

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(District,DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','district']

admin.site.register(Branch, BranchAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Account, AccountAdmin)


class RegisterationAdmin(admin.ModelAdmin):
    list_display =["name",'district','branch','account']
    list_editable = ['account']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Registration, RegisterationAdmin)
