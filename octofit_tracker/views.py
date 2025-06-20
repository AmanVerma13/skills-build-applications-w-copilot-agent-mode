
from rest_framework import viewsets
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.response import Response
from rest_framework import status

# Placeholder in-memory data for demonstration
users = []
teams = []
activities = []
leaderboards = []
workouts = []

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(users)
    def create(self, request):
        users.append(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(teams)
    def create(self, request):
        teams.append(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(activities)
    def create(self, request):
        activities.append(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(leaderboards)
    def create(self, request):
        leaderboards.append(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(workouts)
    def create(self, request):
        workouts.append(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)
