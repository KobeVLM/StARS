#!/usr/bin/env python
"""
Test script to debug database connectivity and user creation issues
Run this from stars_project directory: python debug_db.py
"""
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stars.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User
from django.conf import settings

def test_database_connection():
    """Test database connectivity"""
    print("=== DATABASE CONNECTION TEST ===")
    print(f"Database Engine: {settings.DATABASES['default']['ENGINE']}")
    print(f"Database Name: {settings.DATABASES['default']['NAME']}")
    print(f"Database Host: {settings.DATABASES['default']['HOST']}")
    print(f"Database Port: {settings.DATABASES['default']['PORT']}")
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_user_creation():
    """Test user creation and retrieval"""
    print("\n=== USER CREATION TEST ===")
    
    # Check existing users
    existing_users = User.objects.all()
    print(f"Existing users count: {existing_users.count()}")
    
    for user in existing_users:
        print(f"  - {user.username} ({user.email}) - Created: {user.date_joined}")
    
    # Try to create a test user
    test_username = "testuser123"
    test_email = "test@example.com"
    
    try:
        # Delete if exists
        if User.objects.filter(username=test_username).exists():
            User.objects.filter(username=test_username).delete()
            print(f"Deleted existing test user: {test_username}")
        
        # Create new test user
        print(f"Creating test user: {test_username}")
        user = User.objects.create_user(
            username=test_username,
            email=test_email,
            password="testpass123"
        )
        print(f"✅ Test user created successfully - ID: {user.id}")
        
        # Verify user exists
        saved_user = User.objects.get(username=test_username)
        print(f"✅ User verification successful - Username: {saved_user.username}")
        
        # Clean up
        saved_user.delete()
        print(f"✅ Test user deleted successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ User creation failed: {e}")
        return False

def test_table_structure():
    """Check if auth_user table exists and has correct structure"""
    print("\n=== TABLE STRUCTURE TEST ===")
    
    try:
        cursor = connection.cursor()
        
        # Check if auth_user table exists
        cursor.execute("SHOW TABLES LIKE 'auth_user'")
        tables = cursor.fetchall()
        
        if tables:
            print("✅ auth_user table exists")
            
            # Show table structure
            cursor.execute("DESCRIBE auth_user")
            columns = cursor.fetchall()
            print("Table structure:")
            for column in columns:
                print(f"  - {column[0]} ({column[1]})")
                
        else:
            print("❌ auth_user table does not exist")
            print("Run: python manage.py migrate")
            
    except Exception as e:
        print(f"❌ Table structure check failed: {e}")

if __name__ == "__main__":
    print("StARS Project Database Debug Script")
    print("=" * 40)
    
    # Test database connection
    if test_database_connection():
        # Test table structure
        test_table_structure()
        
        # Test user creation
        test_user_creation()
    
    print("\n=== DEBUG COMPLETE ===")
    print("If all tests pass but registration still doesn't work,")
    print("check the Django server console for DEBUG messages.")