from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_percent = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.year})"
