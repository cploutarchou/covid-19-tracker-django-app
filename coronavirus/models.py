from django.db import models


class DailyStats(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    new_cases = models.IntegerField()
    deaths = models.IntegerField()
    daily_tests = models.IntegerField()
    last_updated = models.DateTimeField()
    updated = models.BooleanField(default=False)
