import secrets

from django.db import models


class New(models.Model):
    news_title = models.CharField(max_length=128)
    news_img = models.TextField(max_length=3000)
    news_desc = models.TextField(max_length=2000)
    news_tag = models.CharField(max_length=128)
    news_token = models.CharField(max_length=32, default=secrets.token_hex(32 // 2))