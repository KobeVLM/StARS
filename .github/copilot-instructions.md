# Copilot Instructions for StARS Project

## Project Overview
StARS is a Django 5.2.6 project in early development stage. This is a fresh Django installation with minimal customization.

## Project Structure
- **Root directory**: `c:\Users\Kobe\Desktop\StARS\`
- **Django project**: `stars_project/` (contains `manage.py`)
- **Main app**: `stars/` (Django project configuration)
- **Working directory**: Always operate from `stars_project/` when running Django commands

## Key Architecture Patterns

### Django Project Layout
```
stars_project/
├── manage.py                 # Django management script
└── stars/                   # Main project configuration
    ├── settings.py          # Project settings
    ├── urls.py              # URL routing
    ├── wsgi.py              # WSGI application
    └── asgi.py              # ASGI application
```

### Development Workflow
- **Django commands**: Run from `stars_project/` directory using `python manage.py <command>`
- **Database**: Currently using SQLite (`db.sqlite3`) - default Django setup
- **Debug mode**: Enabled (`DEBUG = True` in settings)
- **Admin interface**: Available at `/admin/` (default Django admin)

## Important Conventions

### Settings Configuration
- **Secret key**: Uses Django's insecure default (needs updating for production)
- **Database**: SQLite with default configuration
- **Static files**: Standard Django setup with `STATIC_URL = 'static/'`
- **Templates**: Standard Django template configuration (no custom directories)

### URL Patterns
- Main URL configuration in `stars/urls.py`
- Currently only includes Django admin at `/admin/`
- No custom apps or views defined yet

## Development Commands
```bash
# Navigate to Django project directory
cd stars_project

# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

## Current State & Next Steps
This is a minimal Django project with:
- ✅ Basic Django configuration
- ✅ Admin interface setup
- ❌ No custom apps created
- ❌ No models defined
- ❌ No custom views or templates
- ❌ No requirements file or dependency management

When adding new features:
1. Create Django apps using `python manage.py startapp <app_name>`
2. Add apps to `INSTALLED_APPS` in `settings.py`
3. Follow Django's MVT (Model-View-Template) pattern
4. Create URL patterns in app-specific `urls.py` files
5. Include app URLs in the main `urls.py`