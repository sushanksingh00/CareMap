# CareMap

## Overview

CareMap is a Django-based web application designed to help users record, interpret, and track health-related symptoms in a structured, private, and non-diagnostic way. Authenticated users can enter symptoms they are experiencing and receive high-level informational insights generated using an AI language model. Each interaction is stored so users can review their symptom history over time.

The purpose of CareMap is not to diagnose medical conditions or replace professional medical advice. Instead, it serves as a personal health-awareness and symptom journaling tool, helping users notice patterns, reflect on recurring issues, and make more informed decisions about when seeking medical attention may be appropriate.

This project was developed as the final capstone for CS50’s Web Programming with Python and JavaScript.

---

## Distinctiveness and Complexity

CareMap is distinct from all prior CS50W projects in both domain focus and technical design. Unlike Project 4 (Social Network), this application contains no social functionality: users cannot follow others, post publicly, like content, or interact through shared feeds. All data is private and accessible only to the authenticated user. Unlike Project 2 (E-Commerce), CareMap does not involve products, listings, payments, carts, or transactions. Its core purpose is not commercial interaction but structured personal data tracking and interpretation.

What the project is can be described as a personal health information system that combines user authentication, persistent data storage, AI-assisted interpretation, and dynamic frontend behavior. Users submit symptom data, which is processed server-side, passed through a carefully constrained AI prompt, and returned as informational output. Each query is stored chronologically, allowing users to review and reflect on their symptom history over time. This longitudinal tracking component fundamentally differentiates CareMap from simple CRUD applications.

From a complexity perspective, the project goes beyond earlier coursework by integrating multiple non-trivial components. The backend uses Django models to manage users and symptom history, enforces authentication and access control, and securely coordinates interactions with an external AI API. The frontend relies on JavaScript to submit symptom queries asynchronously, render responses dynamically, and update history views without full page reloads. Additionally, the project required careful design decisions to ensure that AI-generated responses remain informational rather than diagnostic, adding both ethical and technical complexity.

Together, these elements form a system that required architectural planning, backend–frontend coordination, and thoughtful constraint of AI behavior, making CareMap both distinct and substantially more complex than previous projects in the course.

---

## Technologies Used

- Python & Django – Backend framework for routing, authentication, models, and database interaction  
- SQLite – Persistent storage for user accounts and symptom history  
- JavaScript – Dynamic frontend behavior and asynchronous requests  
- HTML & CSS – Templating and responsive user interface  
- Gemini API – Generates high-level informational responses based on user-entered symptoms  

Note: An earlier Flask-based prototype of this project is preserved for reference under `_archive/unnecessary/flask_app/`, but the primary and evaluated implementation uses Django, in accordance with CS50W requirements.

---

## File Structure and Contents

- manage.py – Django project entry point used to run the server and manage commands  
- caremap_site/ – Django project configuration directory  
   - settings.py – Project settings, installed apps, middleware, and database configuration  
   - urls.py – Root URL configuration  
   - asgi.py, wsgi.py – ASGI/WSGI entry points  
- caremap/ – Main Django application  
   - apps.py – App configuration  
   - models.py – Defines database models for storing user symptom queries and timestamps  
   - views.py – Handles request logic, form submission, AI API interaction, and response rendering  
   - urls.py – Application-specific URL routes  
   - migrations/ – Django migrations for database schema  
- templates/ – HTML templates for login, registration, symptom input, and history pages  
- static/ – CSS and JavaScript files for styling and frontend interactivity  
- requirements.txt – Python dependencies required to run the Django application  
- db.sqlite3 – SQLite database used for local development  
- _archive/unnecessary/flask_app/ – Archived Flask-based prototype of the project (not part of final evaluation)  
- README.md – Project documentation  

---

## How to Run the Application

1. Clone the repository and navigate into the project directory  
2. Create and activate a virtual environment  
3. Install dependencies using:

   pip install -r requirements.txt

4. Apply database migrations using:

   python manage.py migrate

5. Start the development server using:

   python manage.py runserver

6. Open a browser and visit:

   http://127.0.0.1:8000/

---

## Design Decisions

One key design decision was to keep the user interface minimal and focused. The application is intended to feel like a lightweight assistant rather than a complex medical system, reducing cognitive load and making it accessible to non-technical users.

Another major decision was to use an AI language model rather than a fixed medical database. This allows users to enter symptoms in natural language rather than relying on predefined keywords. To address ethical concerns, the AI prompt is explicitly constrained to provide informational, non-diagnostic responses and encourage professional consultation when appropriate.

Security considerations were also important. Passwords are hashed, sessions are securely managed, and users are restricted to accessing only their own data. Features such as email verification were intentionally excluded to keep the project focused and manageable within the course scope.

---

## Additional Information

CareMap intentionally avoids providing medical diagnoses or treatment recommendations. All output is informational and designed to support awareness rather than decision-making.

A short video demonstration of the application is available here:  
https://www.youtube.com/watch?v=kwQX0F6eih4

---

## Screenshots

Below are three screenshots of the application UI:

![Screenshot 1](Screenshot%202025-12-24%20at%2010.00.53%E2%80%AFPM.png)

![Screenshot 2](Screenshot%202025-12-24%20at%2010.01.20%E2%80%AFPM.png)

![Screenshot 3](Screenshot%202025-12-24%20at%2010.01.32%E2%80%AFPM.png)
