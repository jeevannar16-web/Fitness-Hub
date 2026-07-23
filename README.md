<div align="center">

# Fitness Hub

**Your all-in-one fitness platform for exercises, gear, and daily motivation.**

[![Django](https://img.shields.io/badge/Django-5.0.6-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[Live Demo](#getting-started) | [Report Bug](https://github.com/jeevannar16-web/Fitness-Hub/issues) | [Features](#features)

</div>

---

## Overview

Fitness Hub is a full-featured Django web application designed to help users on their fitness journey. Browse a comprehensive exercise library, shop for premium fitness gear, and stay inspired with daily motivational content.

## Features

- **Exercise Library** — Browse exercises filtered by muscle group and difficulty level
- **Fitness Store** — Shop products across multiple categories with stock tracking
- **Inspiration Feed** — Read quotes, tips, and success stories
- **User Accounts** — Register, login, and manage your profile
- **Admin Panel** — Full admin interface for content management
- **Responsive Design** — Mobile-first UI built with Bootstrap 5
- **AI-Ready** — Integrated LangChain, ChromaDB, and Google Gemini (coming soon)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.0.6 |
| Frontend | Bootstrap 5, Custom CSS |
| Database | SQLite3 |
| Forms | django-crispy-forms |
| Image Processing | Pillow |
| AI (Planned) | LangChain, ChromaDB, Google Gemini |

## Project Structure

```
Fitness-Hub/
├── fitness_hub/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── exercises/            # Exercise library app
│   ├── models.py
│   ├── views.py
│   └── templates/
├── store/                # Fitness store app
│   ├── models.py
│   ├── views.py
│   └── templates/
├── inspiration/          # Inspiration & motivation app
│   ├── models.py
│   ├── views.py
│   └── templates/
├── users/                # User management app
│   ├── models.py
│   ├── views.py
│   └── templates/
├── templates/            # Base templates
├── static/               # CSS, JS, images
├── media/                # User uploads
├── requirements.txt
├── start.sh              # One-click startup (Linux/macOS/Git Bash)
└── start.bat             # One-click startup (Windows CMD/PowerShell)
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Quick Start

**Linux / macOS / Git Bash:**
```bash
git clone https://github.com/jeevannar16-web/Fitness-Hub.git
cd Fitness-Hub
bash start.sh
```

**Windows (CMD or PowerShell):**
```cmd
git clone https://github.com/jeevannar16-web/Fitness-Hub.git
cd Fitness-Hub
start.bat
```

That's it. The script handles everything — virtual environment, dependencies, database, and sample data.

### Manual Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed sample data
python seed_data.py

# Create admin superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

The app will be available at **http://localhost:8000**

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page with hero, features, and highlights |
| Exercises | `/exercises/` | Full exercise library with filters |
| Exercise Detail | `/exercises/<id>/` | Individual exercise with instructions |
| Store | `/store/` | Product catalog with category filters |
| Product Detail | `/store/<id>/` | Product page with stock info |
| Inspiration | `/inspiration/` | Motivational quotes and tips |
| Login | `/accounts/login/` | User login |
| Register | `/accounts/register/` | New account creation |
| Profile | `/accounts/profile/` | User profile management |
| Admin | `/admin/` | Django admin panel |

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
GOOGLE_API_KEY=your-google-api-key    # For AI features (optional)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

**Jeevan Nar** — [GitHub](https://github.com/jeevannar16-web)

---

<div align="center">
Made with Django and Bootstrap 5
</div>
