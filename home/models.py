from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    post = models.CharField(max_length=500)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friends', null=True)

    @classmethod
    def make_friend(cls,current_user, new_friend=None):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        if new_friend:
            friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        print('done')
        friend.users.remove(new_friend)







