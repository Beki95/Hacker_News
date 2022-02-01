from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):

    def _create(self, user_name, password, **extra):
        if not user_name:
            raise ValueError('you have not entered username')
        user = self.model(
            user_name=user_name, **extra
        )
        user.set_password(raw_password=password)
        user.save(using=self.db)

    def create(self, user_name, password):
        return self._create(user_name, password)

    def create_superuser(self, user_name, password):
        return self._create(user_name, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True, error_messages={
            'unique': "A user with that username already exists.",
        })
    upvoted_submissions = models.ManyToManyField('news.News', related_name='users_upvoted')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # is_superuser
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ()

    objects = UserManager()

    def __str__(self):
        return self.user_name
