# encoding:utf-8
from django.db import models
# from datetime import datetime
from django.utils import timezone


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    phone_num = models.CharField(max_length=11)
    password = models.CharField(max_length=32)
    role_code = models.IntegerField()
    comment = models.CharField(max_length=200)
    gender = models.BooleanField(default=1)

    def __str__(self):
        return u'username：%s,gender：%s' % (self.username, str(self.gender))


class Query_code(models.Model):
    query_name = models.CharField(max_length=40, unique=True)
    author = models.CharField(max_length=40)
    code = models.TextField()
    comment = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return u'query_name：%s,author：%s' % (self.query_name, str(self.author))


from django.contrib import admin


# import models

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (u'username', u'role_code')

# admin.site.register(User, UserAdmin)
