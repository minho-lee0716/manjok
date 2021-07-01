from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=300)
    talents = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'


class UserTalentLogs(models.Model):
    user_id = models.ForeignKey(User)

    class Meta:
        db_table = 'user_talent_logs'
