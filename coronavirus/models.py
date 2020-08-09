from django.db import models


class DailyStats(models.Model):
    date = models.DateField()
    new_cases = models.IntegerField(max_length=50)
    deaths = models.IntegerField(max_length=50)
    daily_tests = models.IntegerField(max_length=50)
    last_updated = models.DateTimeField()
    updated = models.BooleanField(default=False)
