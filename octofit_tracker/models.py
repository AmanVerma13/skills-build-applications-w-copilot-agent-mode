from django.db import models

# These models are for Django admin and DRF compatibility, but MongoDB will be used for actual data storage.

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    team_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    points = models.IntegerField()
    timestamp = models.DateTimeField()

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=100)
    total_points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_points = models.IntegerField()
