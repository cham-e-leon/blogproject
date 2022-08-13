from django.db import models

# Create your models here.
# -- Chapter4-3のサンプル ここから --
# classでテーブルを定義する
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
# -- Chapter4-3のサンプル ここまで --

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    def __str__(self):
        return self.title
