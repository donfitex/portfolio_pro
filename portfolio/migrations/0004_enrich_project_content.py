from django.db import migrations

ROWS = [{'description': 'A Django REST Framework project template for building a task-management API and practicing '
                 'a structured backend workflow.',
  'old_description': 'Explore the source, implementation and development notes for todo api on GitHub.',
  'old_title': 'todo api',
  'tech_stack': 'Python, Django REST Framework',
  'title': 'Todo API',
  'url': 'https://github.com/donfitex/todo-api'},
 {'description': 'A REST backend for an online store, organized around customer accounts, product catalogs, '
                 'shopping carts, orders and payments.',
  'old_description': 'A secure RESTful backend for an online store, built with Django and Django REST '
                     'Framework (DRF).',
  'old_title': 'ecommerce api',
  'tech_stack': 'Python, Django REST Framework, PostgreSQL, SQLite',
  'title': 'E-commerce API',
  'url': 'https://github.com/donfitex/ecommerce_api'},
 {'description': 'A profile enrichment API combining gender, age and nationality services with validation, '
                 'idempotent profile creation, filtering and natural-language search.',
  'old_description': 'A Django REST API that classifies names by gender using the Genderize API, with '
                     'additional processing and validation.',
  'old_title': 'gender classifier api',
  'tech_stack': 'Python, Django REST Framework, Requests, SQLite',
  'title': 'Intelligence Query Engine',
  'url': 'https://github.com/donfitex/gender-classifier-api'},
 {'description': 'An authenticated document processing API for uploading PDFs and images, extracting text '
                 'with OCR and keeping documents scoped to their owners.',
  'old_description': 'Explore the source, implementation and development notes for AI document extraction '
                     'API on GitHub.',
  'old_title': 'AI document extraction API',
  'tech_stack': 'Python, Django REST Framework, Tesseract OCR, Celery, Redis',
  'title': 'Document Extraction API',
  'url': 'https://github.com/donfitex/AI-document-extraction-API'},
 {'description': 'An early command-line project workspace. The public repository currently contains its '
                 'introduction and license; implementation details are not yet published.',
  'old_description': 'Explore the source, implementation and development notes for insighta cli on GitHub.',
  'old_title': 'insighta cli',
  'tech_stack': 'Stack not published yet',
  'title': 'Insighta CLI',
  'url': 'https://github.com/donfitex/insighta-cli'},
 {'description': 'A full-stack web application pairing a React interface with a Django REST Framework '
                 'backend.',
  'old_description': 'A full-stack Web App with Django REST Framework and React',
  'old_title': 'Full Stack Web App',
  'tech_stack': 'React, JavaScript, Python, Django REST Framework',
  'title': 'Full-stack Web App',
  'url': 'https://github.com/donfitex/Full-Stack-Web-App'},
 {'description': 'An IBM course capstone repository for dealership browsing and customer reviews, bringing '
                 'together a React frontend, Django services and an Express/MongoDB data layer.',
  'old_description': 'Explore the source, implementation and development notes for xrwvm fullstack developer '
                     'capstone on GitHub.',
  'old_title': 'xrwvm fullstack developer capstone',
  'tech_stack': 'React, JavaScript, Django, Express, MongoDB',
  'title': 'Car Dealership Capstone',
  'url': 'https://github.com/donfitex/xrwvm-fullstack_developer_capstone'},
 {'description': 'A news and magazine publishing platform under development, combining Django content '
                 'management with responsive pages and incremental UI updates.',
  'old_description': 'A production-ready news and magazine platform built with Django',
  'old_title': 'newshub pro',
  'tech_stack': 'Python, Django, PostgreSQL, Bootstrap, HTMX',
  'title': 'NewsHub Pro',
  'url': 'https://github.com/donfitex/newshub-pro'},
 {'description': 'An early project concept for an AI agent that curates global news. The repository '
                 'currently contains its project introduction.',
  'old_description': 'Explore the source, implementation and development notes for Global news AI on GitHub.',
  'old_title': 'Global news AI',
  'tech_stack': 'Google AI Studio · concept',
  'title': 'Global News AI',
  'url': 'https://github.com/donfitex/Global_news_AI'},
 {'description': 'A Python data analysis exercise calculating color frequencies, mean and median '
                 'frequencies, variance, probabilities and Fibonacci totals with PostgreSQL storage.',
  'old_description': '1. Install Python 3 and PostgreSQL.',
  'old_title': 'py statistics',
  'tech_stack': 'Python, PostgreSQL',
  'title': 'Python Statistics Lab',
  'url': 'https://github.com/donfitex/py_statistics'},
 {'description': 'A Django application foundation organized around accounts, vehicles, trips, expenses and '
                 'integrations for mileage tracking.',
  'old_description': 'Explore the source, implementation and development notes for mileage tracker on '
                     'GitHub.',
  'old_title': 'mileage tracker',
  'tech_stack': 'Python, Django REST Framework, PostgreSQL, Celery, Redis, GeoPy',
  'title': 'Mileage Tracker',
  'url': 'https://github.com/donfitex/mileage_tracker'},
 {'description': 'An ASP.NET Core MVC application foundation with Razor views, a shared responsive layout '
                 'and Bootstrap styling.',
  'old_description': 'Explore the source, implementation and development notes for shopsphere on GitHub.',
  'old_title': 'shopsphere',
  'tech_stack': 'C#, ASP.NET Core, Razor, Bootstrap, jQuery',
  'title': 'ShopSphere',
  'url': 'https://github.com/donfitex/shopsphere'},
 {'description': 'A browser-based task manager with priorities, due dates, drag-and-drop ordering, search, '
                 'progress tracking, themes and local backup and restore.',
  'old_description': 'A clean, fast todo list that runs entirely in the browser. No installs, no build step, '
                     'no dependencies.',
  'old_title': 'todo app',
  'tech_stack': 'HTML, CSS, JavaScript, Local Storage',
  'title': 'Tasks',
  'url': 'https://github.com/donfitex/todo-app'},
 {'description': 'An online store with product browsing, saved items, cart and checkout, order history, '
                 'merchant administration and payment integration.',
  'old_description': '2. Copy `.env.example` to `.env` and fill it in (Supabase, Mailgun, ADMIN_EMAILS, '
                     'optional Paystack and WhatsApp number).',
  'old_title': 'e Shop',
  'tech_stack': 'React, Vite, Tailwind CSS, Express, Supabase',
  'title': 'R-Blink Shop',
  'url': 'https://github.com/donfitex/e_Shop'},
 {'description': 'A collaboration platform prototype combining channels, threaded conversations, social '
                 'posts, recruitment and peer-to-peer voice and video rooms.',
  'old_description': 'Built in Step 1 (all covered by `npm test`):',
  'old_title': 'rblink.chat',
  'tech_stack': 'JavaScript, Node.js, WebSocket, WebRTC',
  'title': 'R-Blink Chat',
  'url': 'https://github.com/donfitex/rblink.chat'},
 {'description': 'A research prototype for voice-based maternal health information in Yoruba, Hausa, Igbo '
                 'and English, combining speech, translation and retrieval-augmented answers.',
  'old_description': 'Research prototype: speech-in, speech-out maternal health Q&A for Yoruba, Hausa, Igbo '
                     'and English, built',
  'old_title': 'mama voice',
  'tech_stack': 'Python, FastAPI, Ollama, RAG, Speech-to-text, Text-to-speech',
  'title': 'MamaVoice',
  'url': 'https://github.com/donfitex/mama-voice'},
 {'description': 'A developer portfolio with project case studies, an experience timeline and a searchable '
                 'project explorer backed by Django and vector-enabled PostgreSQL.',
  'old_description': 'Explore the source, implementation and development notes for portfolio on GitHub.',
  'old_title': 'portfolio',
  'tech_stack': 'Next.js, TypeScript, Tailwind CSS, Django REST Framework, PostgreSQL, pgvector',
  'title': 'Developer Portfolio · Next.js',
  'url': 'https://github.com/donfitex/portfolio'},
 {'description': 'A sports talent marketplace in development, connecting athlete profiles and performance '
                 'with scouting, recruitment opportunities and organization workspaces.',
  'old_description': '- Web frontend: Next.js + TypeScript + Tailwind CSS',
  'old_title': 'athletehub ai',
  'tech_stack': 'Next.js, TypeScript, Tailwind CSS, Django REST Framework, PostgreSQL',
  'title': 'AthleteHub AI',
  'url': 'https://github.com/donfitex/athletehub-ai'},
 {'description': 'My GitHub profile and developer introduction, with an overview of my engineering '
                 'background, skills, current work and featured projects.',
  'old_description': '- **Languages:** Python, JavaScript, TypeScript, SQL, HTML, CSS',
  'old_title': 'donfitex',
  'tech_stack': 'Markdown, GitHub',
  'title': 'Developer Profile',
  'url': 'https://github.com/donfitex/donfitex'},
 {'description': 'An election data explorer with polling-unit results, local government totals and validated '
                 'result entry, using the supplied Delta State test dataset.',
  'old_description': 'Three pages on top of the `bincom_test.sql` database (Delta State, 2011 dummy '
                     'results).',
  'old_title': 'election results',
  'tech_stack': 'Python, Django, JavaScript, SQLite, MySQL',
  'title': 'Election Results Explorer',
  'url': 'https://github.com/donfitex/election_results'},
 {'description': 'A fleet and vehicle operations platform with organization-scoped data, role-based '
                 'membership, reporting and a documented REST API.',
  'old_description': 'FleetOps Cloud is a professional, scalable, secure, multi-tenant SaaS platform for '
                     'fleet and vehicle operations management built with Python, Django, PostgreSQL, '
                     'Tailwind CSS, HTMX, Alpine.js, and Chart.js.',
  'old_title': 'Fleetops Cloud',
  'tech_stack': 'Python, Django, PostgreSQL, HTMX, Alpine.js, Chart.js',
  'title': 'FleetOps Cloud',
  'url': 'https://github.com/donfitex/Fleetops-Cloud'},
 {'description': 'A URL shortener with collision-safe codes, click counts, optional expiration, a JSON API '
                 'and validation of unsafe destinations.',
  'old_description': 'A production-ready URL shortener built with Flask. Paste a long link, get a short one, '
                     'share it.',
  'old_title': 'CodeAlpha url shortener',
  'tech_stack': 'Python, Flask, PostgreSQL, Tailwind CSS, Docker',
  'title': 'LinkForge',
  'url': 'https://github.com/donfitex/CodeAlpha_url-shortener'},
 {'description': 'An HR platform for employee records, attendance, leave requests, reviewed payroll, private '
                 'documents and audit reporting.',
  'old_description': 'HROS manages employee records, attendance, leave, reviewed payroll, private employee '
                     'documents, notifications, and audit reporting. It runs as a Django modular monolith '
                     'with PostgreSQL in production and SQLite for development.',
  'old_title': 'zesthr django',
  'tech_stack': 'Python, Django, PostgreSQL, SQLite',
  'title': 'HROS · Human Resources',
  'url': 'https://github.com/donfitex/zesthr-django'},
 {'description': 'A restaurant operations platform connecting menus, orders, kitchen workflows, '
                 'reservations, inventory and branch reporting with role-based staff access.',
  'old_description': 'A modular Django platform for restaurant and branch operations: menus, ordering, '
                     'kitchen workflow, reservations, table management, recipes, inventory, payments, '
                     'reporting, and staff permissions.',
  'old_title': 'RestaurantOS',
  'tech_stack': 'Python, Django, PostgreSQL, Docker',
  'title': 'RestaurantOS',
  'url': 'https://github.com/donfitex/RestaurantOS'},
 {'description': 'An event registration and management platform built around a Django application and REST '
                 'API.',
  'old_description': 'Event registration and management platform built with Django and DRF.',
  'old_title': 'event hub',
  'tech_stack': 'Python, Django, Django REST Framework',
  'title': 'EventHub',
  'url': 'https://github.com/donfitex/event_hub'},
 {'description': 'A recruitment platform for job discovery, private resumes, company hiring pipelines, '
                 'interview scheduling and candidate notifications.',
  'old_description': 'A Django recruitment platform with job discovery, company hiring workspaces,',
  'old_title': 'talent bridge',
  'tech_stack': 'Python, Django, PostgreSQL, Neon, Docker',
  'title': 'TalentBridge',
  'url': 'https://github.com/donfitex/talent-bridge'},
 {'description': 'An e-commerce API project exploring typed HTTP services, fault-tolerant data aggregation, '
                 'asynchronous order processing, semantic search and observability.',
  'old_description': 'A tested, secured, observable e-commerce API with asynchronous order processing,',
  'old_title': 'obs e com',
  'tech_stack': 'TypeScript, Node.js, Express',
  'title': 'Observable Commerce API',
  'url': 'https://github.com/donfitex/obs-e-com'},
 {'description': 'A multi-category storefront and commerce API with product discovery, cart and checkout, '
                 'payment verification, delivery tracking and merchant tools.',
  'old_description': 'Requires Node.js 22+, npm and Docker Compose v2.',
  'old_title': 'e com glo',
  'tech_stack': 'TypeScript, Next.js, Express, PostgreSQL, Prisma, Redis',
  'title': 'E-com Global',
  'url': 'https://github.com/donfitex/e-com-glo'}]

def enrich(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    for row in ROWS:
        for project in Project.objects.filter(github_link=row['url']):
            changed = []
            for field in ('title', 'description'):
                if getattr(project, field) == row['old_' + field]:
                    setattr(project, field, row[field])
                    changed.append(field)
            if not project.tech_stack:
                project.tech_stack = row['tech_stack']
                changed.append('tech_stack')
            if changed:
                project.save(update_fields=changed)

class Migration(migrations.Migration):
    dependencies = [('portfolio', '0003_project_tech_stack')]
    operations = [migrations.RunPython(enrich, migrations.RunPython.noop)]
