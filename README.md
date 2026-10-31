# Raphael Eze · Portfolio

Django portfolio with a responsive gallery, search, featured/live filters, light/dark themes, contact inbox and authenticated owner studio. One service serves the frontend, API, static assets and admin. PostgreSQL in production; SQLite for local development.

## Run

Use Python 3.12. `python -m venv .venv`, activate it, then `pip install -r requirements.txt`.
Set `DEBUG=true` locally and `SECRET_KEY` to a random value (see `.env.example`; export variables in your shell — dotenv is not automatically loaded).
Run `python manage.py migrate`, `python manage.py seed_portfolio`, `python manage.py createsuperuser`, then `python manage.py runserver`.

## Edit your portfolio

Open `/admin/` and sign in with your own superuser. Edit projects, descriptions, comma-separated technology stacks, categories, source/live/video demo and GitHub README links, featured status, publishing and display order. Add About and Skills entries. Contact messages appear in the private Contacts inbox; they are stored in the database, not emailed. Public visitors do not need an account. Only staff can edit; no public signup.

The seed contains all public GitHub repositories reviewed at setup, with live URLs from repository READMEs and connected Render services. Private repositories are excluded from publication. Links are supplied by those sources and may be unavailable if an external host is sleeping. No demo URL is invented. The initial seed never overwrites edits or deletes projects; adding future repositories requires adding a Project in the studio or updating the reviewed JSON seed. A real resume can be linked after you supply one; the original PDF was empty.

## Render + Neon

Build: `bash build.sh`. Start: `bash start.sh`. Deploy branch: **main** in this repository.
Set `SECRET_KEY` (random), `DATABASE_URL` (Neon URL, sslmode=require), `DEBUG=false`, `ALLOWED_HOSTS` (your exact Render/custom hostnames). Render's external hostname is included automatically. Health check: `/health/` tests database connectivity. Migrations and idempotent seed run on startup. Never use SQLite on Render's ephemeral disk.

Create the owner account once from Render Shell with `python manage.py createsuperuser`, or set secure Render environment variables `OWNER_USERNAME`, `OWNER_EMAIL`, `OWNER_PASSWORD` and redeploy. Remove `OWNER_PASSWORD` after the first successful deploy. Existing account passwords are never overwritten. No shared password or default administrator is shipped. Back up Neon regularly. The contact throttle is per-process cache based; use a shared cache if scaling to multiple instances. Free Render instances can sleep when idle.

## Verify

`DEBUG=true python manage.py test` and `SECRET_KEY=<random> python manage.py check --deploy`.
