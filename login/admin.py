from django.contrib import admin
from login.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'contact', 'city')

    def bio(self, obj):
        return obj.bio

    def contact(self, obj):
        return obj.phone

    def city(self, obj):
        return obj.location


admin.site.register(UserProfile , UserProfileAdmin)

