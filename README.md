# StARS

A small Django project to help students and emerging artists practice, share, and grow in a supportive, low-pressure environment.

## Quick overview

- Project: **STARS: Student Artist Space**: An Art-Sharing Platform for Students
- Purpose: STARS **(Student Artist Space)** is a gamified art-sharing platform designed to help students and beginner artists build consistent creative habits in a supportive and collaborative environment. Unlike traditional art platforms that focus on professional exposure or competition, STARS emphasizes learning, sharing, and community engagement. By integrating gamification and peer interaction, the platform encourages motivation, growth, and confidence—empowering emerging artists to develop their skills while celebrating creativity free from external pressure.

## Tech stack

- Python 3.8+
- Django 4.x/5.x
- PostgreSQL (default dev database)

## Setup & run instructions

1. Clone the repository and enter the project folder (CMD):

```cmd
git clone https://github.com/KobeVLM/CSIT327-G6-StARS.git
cd CSIT327-G6-StARS\stars_project
```

```cmd
git clone https://github.com/KobeVLM/CSIT327-G6-StARS.git
cd CSIT327-G6-StARS\stars_project
```

2. Create and activate a Python virtual environment (CMD):

```cmd
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies (CMD):

```cmd
pip install -r requirements.txt
```

4. Apply database migrations (CMD):

```cmd
python manage.py migrate
```

6. Run the development server (CMD):

```cmd
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

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
