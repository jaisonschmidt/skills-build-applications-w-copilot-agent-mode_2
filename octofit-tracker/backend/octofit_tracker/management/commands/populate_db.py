from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Remove existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index for email
        db.users.create_index([("email", 1)], unique=True)

        # Teams
        marvel_team = {"name": "Marvel", "members": ["Iron Man", "Captain America", "Thor", "Hulk"]}
        dc_team = {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman", "Flash"]}
        db.teams.insert_many([marvel_team, dc_team])

        # Users
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Thor", "email": "thor@marvel.com", "team": "Marvel"},
            {"name": "Hulk", "email": "hulk@marvel.com", "team": "Marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Flash", "email": "flash@dc.com", "team": "DC"},
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Superman", "activity": "Cycling", "duration": 45},
            {"user": "Batman", "activity": "Swimming", "duration": 25},
            {"user": "Wonder Woman", "activity": "Yoga", "duration": 60},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 120},
            {"team": "DC", "points": 110},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"user": "Iron Man", "workout": "Chest Press", "reps": 20},
            {"user": "Superman", "workout": "Deadlift", "reps": 15},
            {"user": "Thor", "workout": "Squat", "reps": 25},
            {"user": "Flash", "workout": "Sprints", "reps": 10},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
