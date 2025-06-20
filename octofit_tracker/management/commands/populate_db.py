from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data based on monafit tracker example
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": "team1"},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": "team1"},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass", "team_id": "team2"},
        ]
        teams = [
            {"_id": "team1", "name": "Red Rockets", "members": ["alice@example.com", "bob@example.com"]},
            {"_id": "team2", "name": "Blue Blasters", "members": ["carol@example.com"]},
        ]
        activities = [
            {"user_id": "alice@example.com", "activity_type": "run", "duration": 30, "points": 10, "timestamp": "2025-06-20T08:00:00Z"},
            {"user_id": "bob@example.com", "activity_type": "walk", "duration": 60, "points": 8, "timestamp": "2025-06-20T09:00:00Z"},
            {"user_id": "carol@example.com", "activity_type": "strength", "duration": 45, "points": 12, "timestamp": "2025-06-20T10:00:00Z"},
        ]
        leaderboard = [
            {"team_id": "team1", "total_points": 18},
            {"team_id": "team2", "total_points": 12},
        ]
        workouts = [
            {"name": "Pushups", "description": "Do 20 pushups", "suggested_points": 5},
            {"name": "Jogging", "description": "Jog for 30 minutes", "suggested_points": 10},
        ]

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
