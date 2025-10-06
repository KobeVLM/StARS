# StARS

A small Django project to help students and emerging artists practice, share, and grow in a supportive, low-pressure environment.

## Quick overview

- Project: StARS (Student ARtS)
- Purpose: Provide a simple social platform for students/artists to post practice work, blog entries, and receive feedback.
- Stack: Python, Django, SQLite (default)

## Tech stack

- Python 3.8+
- Django 4.x/5.x (project currently uses a fresh Django install)
- PostgreSQL (default dev database)

## Local setup (Windows)

All commands below assume you're in the repository root. The project Django folder is `stars_project`.

1. Create and activate virtualenv

```powershell
cd stars_project
python -m venv venv
venv\Scripts\Activate.ps1
```

If using cmd.exe instead of PowerShell:

```cmd
venv\Scripts\activate
```

2. Install project dependencies

```powershell
pip install -r requirements.txt  # if present
pip install django
```

3. Apply database migrations

```powershell
python manage.py migrate
```

4. (Optional) Create admin user

```powershell
python manage.py createsuperuser
```

5. Run development server

```powershell
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

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

## Development workflow

- Branches: `feature/<short-description>`, `fix/<short-description>`, `docs/<short-description>`
- Commits: Use Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, etc.)

Before creating a PR:

1. Pull the latest main

```powershell
git checkout main; git pull origin main
git checkout -b feature/your-feature
```

2. Run the app locally and make sure tests (if any) pass.

## Commands (common)

```powershell
cd stars_project
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp app_name
```

## Contributing

- Fork the repo
- Create a feature branch
- Make changes and write tests where appropriate
- Open a PR with a clear description and testing steps

## License

No license is currently specified. Add a LICENSE file (e.g., MIT) if you intend to make this project open source.

---

If you'd like, I can:

- add a `requirements.txt` (minimal: `Django`),
- add a `LICENSE` file (MIT template), or
- fill in team member names/emails and the deployed URL.
