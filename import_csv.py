import os
import django
import csv

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sam_media_analytics.settings')

# Initialize Django
django.setup()

from analytics.models import User

def import_csv(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            User.objects.create(
                user_id=row['user_id'],
                subscription_date=row['subscription_date'],
                phone_operator=row['phone_operator'],
                os_name=row['os_name'],
                os_version=row['os_version'],
                affiliate=row['affiliate'],
                unsubscription_date=row['unsubscription_date'],
                service=row['service'],
                aggregator=row['aggregator']
            )

# Set path to a file
import_csv('data/users.csv')
