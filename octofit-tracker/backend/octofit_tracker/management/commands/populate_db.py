import logging
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId
from datetime import timedelta

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        logging.debug("Starting database population...")

        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password1"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password2"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password3"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password4"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password5"},
        ]
        db.users.insert_many(users)

        # Debugging: Log user creation
        logging.debug("Creating users...")
        for user in users:
            logging.debug(f"User: {user}")

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Debugging: Log team creation
        logging.debug("Creating teams...")
        logging.debug(f"Team 1: {teams[0]}")
        logging.debug(f"Team 2: {teams[1]}")

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 3600},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 7200},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 5400},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 1800},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 4500},
        ]
        db.activity.insert_many(activities)

        # Debugging: Log activities creation
        logging.debug("Creating activities...")
        for activity in activities:
            logging.debug(f"Activity: {activity}")

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Debugging: Log leaderboard entries creation
        logging.debug("Creating leaderboard entries...")
        for entry in leaderboard:
            logging.debug(f"Leaderboard Entry: {entry}")

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        # Debugging: Log workouts creation
        logging.debug("Creating workouts...")
        for workout in workouts:
            logging.debug(f"Workout: {workout}")

        logging.debug("Database population completed.")
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))