
from django.db import models


class CarnewsCarnews(models.Model):
    news_title = models.CharField(max_length=50, blank=True, null=True)
    news_time_str = models.CharField(max_length=20, blank=True, null=True)
    news_art_time = models.CharField(max_length=32, blank=True, null=True)
    news_list_img = models.CharField(max_length=100, blank=True, null=True)
    news_path = models.CharField(max_length=100, blank=True, null=True)
    news_read_num = models.CharField(max_length=20, blank=True, null=True)
    news_comment_num = models.CharField(max_length=20, blank=True, null=True)
    news_abstract = models.TextField(blank=True, null=True)
    news_art_img = models.TextField(blank=True, null=True)
    news_art_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CarNews_carnews'



