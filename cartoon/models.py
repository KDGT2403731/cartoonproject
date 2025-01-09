from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class Cartoon(models.Model):
    era = models.CharField("時代", max_length=100)
    thumbnail = models.ImageField("画像", null=True, blank=True)
    year = models.CharField("年間", max_length=100)
    description = models.TextField("説明", )

    def __str__(self):
        return self.era
    
class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=RATE_CHOICES)
    is_spoiler = models.BooleanField(default=False)  # ネタバレフラグ
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title