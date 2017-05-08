from django.contrib import admin
from custom_user.models import User as MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('affiliation',)}),
    )


admin.site.register(MyUser, MyUserAdmin)
