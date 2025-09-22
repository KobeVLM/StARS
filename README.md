# StARS - Student Django Project

## About
Empowering students and emerging artists to **practice**, **share**, and **grow** in a supportive, collaborative, and fun environment—without the pressure of competition.

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)
- Git

## Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/KobeVLM/StARS.git
cd StARS
```

### 2. Create a Virtual Environment
```bash
# Create virtual environment
cd stars_project

python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Navigate to the Django Project
```bash
cd stars_project
```

### 5. Set Up the Database
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Git Workflow Guidelines

### Branch Naming Convention
- **Features**: `feature/<short-description>`
  - Example: `feature/user-authentication`
- **Bug fixes**: `fix/<short-description>`
  - Example: `fix/login-validation`
- **Documentation**: `docs/<short-description>`
  - Example: `docs/update-readme`

### Commit Message Convention
We use [Conventional Commits](https://www.conventionalcommits.org/) for clear and consistent commit messages:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

**Examples:**
```
feat: add user registration form
fix: resolve login redirect issue
docs: update installation instructions
chore: update dependencies
```

### Pull Request Process

Before creating a pull request, ensure you:

1. **Pull the latest changes from main:**
   ```bash
   git checkout main
   git pull origin main
   git checkout your-branch-name
   git merge main
   ```

2. **Ensure the project runs without errors:**
   ```bash
   cd stars_project
   python manage.py runserver
   ```

3. **Write a clear PR description** that includes:

   - What changes were made
   - Why the changes were necessary
   - Any testing performed
   - Screenshots (if applicable)

4. **Create the pull request** and wait for code owner review

### Code Review
- All pull requests require review and approval from the code owner
- Address any feedback before the PR can be merged
- Keep discussions professional and constructive

## Development Commands

### Common Django Commands
```bash
# Start development server
python manage.py runserver

# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Create a new Django app
python manage.py startapp app_name
```

## Contributing
1. Fork the repository
2. Create a feature branch following our naming convention
3. Make your changes
4. Follow our commit message convention
5. Submit a pull request

**No license is currently specified for this project. All rights reserved by the repository owner. If you wish to use, modify, or distribute this code, please contact *KobeVLM* for permission.**
