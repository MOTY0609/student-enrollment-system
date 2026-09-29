Student Enrollment System
A full-stack Django web application built for the MOTY Scholarship Initiative, allowing students to create an account and enroll for a scholarship program. Built and deployed as part of a SIWES (Student Industrial Work Experience Scheme) placement.
🔗 Live Demo: https://student-enrollment-system-567p.onrender.com/

📖 Overview
Organizations offering scholarships need a structured way to collect and manage applications. This system provides students with a simple, secure platform to:
Create an account and log in
View the list of currently enrolled students
Register (enroll) for the scholarship if they haven't already

✨ Features
🔐 User registration, login, and logout (Django's built-in authentication)
🛡️ Protected views — only authenticated users can access enrollment features
📋 Live enrollment list showing all registered students
📝 Scholarship registration form with validation
🛠️ Customized Django Admin panel for managing student records
🎨 Fully styled front end with custom CSS

🛠️ Tech Stack
Backend: Django (Python)
Database (Production): PostgreSQL
Database (Development): SQLite
Frontend: Django Template Language + CSS3
Production Server: Gunicorn
Static Files: WhiteNoise
Hosting: Render

🚀 Getting Started (Local Setup)
Prerequisites
Python 3.10+
pip
Git

Installation
# Clone the repository
git clone https://github.com/MOTY0609/student-enrollment-system.git
cd student-enrollment-system

# Create and activate a virtual environment
python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file in the project root with:
# SECRET_KEY=your-secret-key-here
# DEBUG=True
# ALLOWED_HOSTS=127.0.0.1,localhost

# Run migrations
python manage.py migrate

# Create a superuser (for admin access)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.
📁 Project Structure
├── [project_name]/        # Project configuration (settings, URLs, WSGI)
├── [app_name]/             # Main application (models, views, forms, templates)
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── static/                 # CSS and static assets
├── build.sh                 # Render build script
├── requirements.txt
└── manage.py

🌐 Deployment
This project is deployed on Render. Configuration is managed via environment variables:
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DATABASE_URL
Static files are served using WhiteNoise, and the app runs in production via Gunicorn.

👤 Author
Anosike Kehinde
SIWES Industrial Training — Student Enrollment System Project
📄 License
This project was built for educational and training purposes as part of a SIWES placement.
