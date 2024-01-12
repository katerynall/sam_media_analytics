from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=40)
    subscription_date = models.CharField(max_length=40)
    phone_operator = models.CharField(max_length=3)
    os_name = models.CharField(max_length=10)
    os_version = models.CharField(max_length=10)
    affiliate = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    unsubscription_date = models.CharField(max_length=40)
    service = models.CharField(max_length=10)
    aggregator = models.CharField(max_length=10)
