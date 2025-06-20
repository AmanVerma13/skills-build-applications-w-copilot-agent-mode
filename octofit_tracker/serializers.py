from rest_framework import serializers

# Serializers for users, teams, activity, leaderboard, and workouts collections

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    team_id = serializers.CharField(allow_null=True, required=False)

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField(), required=False)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    activity_type = serializers.CharField()
    duration = serializers.IntegerField()
    points = serializers.IntegerField()
    timestamp = serializers.DateTimeField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    team_id = serializers.CharField()
    total_points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    suggested_points = serializers.IntegerField()
