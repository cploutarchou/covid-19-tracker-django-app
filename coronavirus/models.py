import datetime

from django.db import models


class JobsLogs(models.Model):
    id = models.AutoField(primary_key=True)
    started_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    completed_at = models.DateTimeField()
    task_names = models.CharField(max_length=100)
    data = models.TextField()
    status = models.CharField(max_length=100)
    executed = models.BooleanField(default=False)


class DailyStats(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    new_cases = models.IntegerField()
    deaths = models.IntegerField()
    daily_tests = models.IntegerField()
    last_updated = models.DateTimeField()
    updated = models.BooleanField(default=False)
