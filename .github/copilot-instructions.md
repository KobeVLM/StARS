# Copilot Instructions for StARS Project

## Project Overview
StARS is a Django 5.2.6 student project in early development stage. This is a fresh Django installation with minimal customization but follows established development workflows and conventions.

## Project Structure
- **Root directory**: `c:\Users\Kobe\Desktop\StARS\`
- **Django project**: `stars_project/` (contains `manage.py`)
- **Main app**: `stars/` (Django project configuration)
- **Working directory**: Always operate from `stars_project/` when running Django commands

## Key Architecture Patterns

### Django Project Layout
```
StARS/
├── README.md                # Project documentation
├── .github/
│   └── copilot-instructions.md
└── stars_project/
    ├── manage.py            # Django management script
    ├── venv/               # Virtual environment (local only)
    └── stars/              # Main project configuration
        ├── settings.py     # Project settings
        ├── urls.py         # URL routing
        ├── wsgi.py         # WSGI application
        └── asgi.py         # ASGI application
```

### Development Environment Setup
- **Virtual environment**: Located at `stars_project/venv/`
- **Activation**: Use `venv\Scripts\activate` on Windows
- **Dependencies**: Install with `pip install django` (minimal setup)
- **Database setup**: Run `python manage.py migrate` before first use

## Development Workflow

### Essential Commands (from `stars_project/` directory)
```bash
# Environment setup
python -m venv venv
venv\Scripts\activate
pip install django

# Django operations
python manage.py runserver      # Start development server
python manage.py migrate        # Apply database migrations
python manage.py makemigrations # Create new migrations
python manage.py createsuperuser # Create admin user
python manage.py startapp <name> # Create new Django app
```

### Git Workflow Conventions
- **Branch naming**:
  - Features: `feature/<short-description>`
  - Bug fixes: `fix/<short-description>`
  - Documentation: `docs/<short-description>`

- **Commit messages** (Conventional Commits):
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation
  - `chore:` for maintenance
  - `style:` for formatting
  - `refactor:` for code restructuring
  - `test:` for adding tests

### Pull Request Requirements
1. Pull latest changes from main branch
2. Ensure project runs without errors (`python manage.py runserver`)
3. Write clear PR description with what/why/testing details
4. Wait for code owner review and approval

## Important Conventions

### Settings Configuration
- **Secret key**: Uses Django's insecure default (needs updating for production)
- **Database**: SQLite with default configuration
- **Static files**: Standard Django setup with `STATIC_URL = 'static/'`
- **Templates**: Standard Django template configuration (no custom directories yet)

### URL Patterns
- Main URL configuration in `stars/urls.py`
- Currently only includes Django admin at `/admin/`
- No custom apps or views defined yet

## Current State & Next Steps
This is a minimal Django project with established workflows:
- ✅ Basic Django configuration
- ✅ Admin interface setup
- ✅ Development workflow documented
- ✅ Git conventions established
- ✅ Virtual environment setup
- ❌ No custom apps created
- ❌ No models defined
- ❌ No custom views or templates
- ❌ No requirements.txt file

When adding new features:
1. Create feature branch: `git checkout -b feature/<description>`
2. Create Django apps: `python manage.py startapp <app_name>`
3. Add apps to `INSTALLED_APPS` in `settings.py`
4. Follow Django's MVT (Model-View-Template) pattern
5. Create URL patterns in app-specific `urls.py` files
6. Include app URLs in main `urls.py`
7. Use conventional commit messages
8. Follow PR process for code review

## Development Server Access
- **Local URL**: `http://127.0.0.1:8000/`
- **Admin interface**: `http://127.0.0.1:8000/admin/`
- **Default port**: 8000 (Django default)