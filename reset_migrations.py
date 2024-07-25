import os
import django
from django.db import connection

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobber.settings')  # Replace with your actual project settings
django.setup()

app_name = 'applicants'  # Replace with your actual app name

with connection.cursor() as cursor:
    cursor.execute(f"DELETE FROM django_migrations WHERE app = '{app_name}';")

print(f"Deleted migration records for app: {app_name}")


from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS applicants_customuser")

print("Deleted the 'applicants_profile table")
