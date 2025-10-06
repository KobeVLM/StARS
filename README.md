# StARS

A small Django project to help students and emerging artists practice, share, and grow in a supportive, low-pressure environment.

## Quick overview

- Project: StARS (Student Art Sharing System)
- Purpose: Provide a simple social platform for students/artists to post practice work, blog entries, and receive feedback.
- Stack: Python, Django, SQLite (default)

## Tech stack

- Python 3.8+
- Django 4.x/5.x (project currently uses a fresh Django install)
- PostgreSQL (default dev database)

## Setup & run instructions

Instructions below assume someone has just cloned the repository and wants to run the project locally on Windows for the first time. We'll use the `stars_project` folder as the Django project root.

1. Open a terminal and change into the project folder

```powershell
cd path\to\repo\stars_project
```

2. Create a Python virtual environment and activate it

PowerShell (recommended):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Command Prompt (cmd.exe):

```cmd
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

If the repository contains `requirements.txt`:

```powershell
pip install -r requirements.txt
```

If not, install Django and the common DB packages used by the project:

```powershell
pip install django psycopg2-binary dj-database-url
```

4. Configure environment variables (optional)

If you're using Supabase or another Postgres DB, set `DATABASE_URL` in your environment before running migrations. Example (PowerShell):

```powershell
#$env:DATABASE_URL = '<your-postgres-connection-uri>'  # one-time for current session
setx DATABASE_URL "<your-postgres-connection-uri>"   # persist for the user (new shells)
```

5. Apply database migrations

```powershell
python manage.py migrate
```

6. (Optional) Create an admin user for the Django admin

```powershell
python manage.py createsuperuser
```

7. Run the development server

```powershell
python manage.py runserver
```

Open your browser to http://127.0.0.1:8000/ to see the site.

Troubleshooting quick tips:

- If you see import errors, ensure your virtualenv is activated and packages installed.
- If migrations fail against Supabase/Postgres, verify `DATABASE_URL` and that your Supabase DB allows external connections.
- For persistent environment variables in PowerShell, use `setx` and restart your terminal.

## Project structure (important files)

- `stars_project/manage.py` — Django management script
- `stars_project/stars/` — Django project settings and URLs
- `stars_project/accounts/` — main app (models, views, templates)
- `static/` and `templates/` — front-end assets and templates

## Team

Please replace the placeholders with real names/emails for your team members.

- Kobe (Lead) — KobeVLM, email: your-email@domain
- Member 2 — Name, role, email
- Member 3 — Name, role, email

## Deployment

- Deployed site: (**NOT YET DEPLOYED**)

## Git Workflow Guidelines

This project follows simple Git conventions to keep history clean and collaboration easy. Please follow these guidelines when creating branches, writing commits, and opening pull requests.

Branch naming:

- Features: `feature/<short-description>` (example: `feature/user-authentication`)
- Bug fixes: `fix/<short-description>` (example: `fix/login-validation`)
- Documentation: `docs/<short-description>` (example: `docs/update-readme`)

Commit messages (Conventional Commits):

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

Examples:

```
feat: add user registration form
fix: resolve login redirect issue
docs: update installation instructions
chore: update dependencies
```

Pull Request process:

1. Pull the latest changes from main:

```powershell
git checkout main
git pull origin main
git checkout your-branch-name
git merge main
```

2. Ensure the project runs without errors (run server and any tests):

```powershell
cd stars_project
python manage.py runserver
```

3. Write a clear PR description including what changed, why, and testing steps.
4. Create the PR and request review from the code owner(s). Address feedback before merging.

Code review:

- All pull requests require at least one approving review from a code owner.
- Keep discussions respectful and focused on the code.
- Small, well-scoped PRs are easier to review and land quickly.
