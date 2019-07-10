from django.contrib import admin
from home.models import Post
# Register your models here.
from home.models import Friend
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')

    def user(self, obj):
        return obj.user

    def post(self, obj):
        return obj.created



admin.site.register(Post)

admin.site.register(Friend)
# Register your models here.