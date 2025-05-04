🛡️ Web Vulnerability Scanner Prototype

A lightweight Django-based web application that detects common web vulnerabilities like **Cross-Site Scripting (XSS)** and **SQL Injection** using custom pattern matching. It also provides an interactive dashboard for viewing scan results and user-submitted reports.

---

## 📌 Project Overview

This project is designed to demonstrate how basic web security scanners can be implemented to raise awareness about insecure coding practices. It scans user-input URLs and HTML forms for known vulnerability patterns using custom regular expressions.

---

## 🚀 Features

- 🔍 Scan for **XSS** and **SQL Injection** vulnerabilities.
- 📊 Interactive dashboard to view and manage scan results.
- 📥 Allow users to submit URLs or code snippets for testing.
- 🧠 Custom regex rules for detection logic.
- 💡 Educational tool for web security awareness.

---

## 🛠️ Tech Stack

- **Django** – Backend framework
- **Python** – Core logic and regex-based scanning
- **HTML/CSS** – Frontend design
- **SQLite** – Lightweight database for storing reports
- **Bootstrap** – Styling and responsive UI

---

## 📂 Project Structure

WebScanner/
├── scanner/
│ ├── templates/
│ │ └── dashboard.html
│ ├── static/
│ │ └── style.css
│ ├── views.py
│ ├── models.py
│ └── urls.py
├── WebScanner/
│ └── settings.py
├── db.sqlite3
├── manage.py
└── requirements.txt


---

## 🔧 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vedant-lab-15/Webscan.git
cd Webscan

2. Create and Activate a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows

3. Install Dependencies

pip install -r requirements.txt

    If requirements.txt is missing, use:

pip install django

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Run the Server

python manage.py runserver

Then open http://127.0.0.1:8000 in your browser.
🔍 How It Works

    The user submits a URL or HTML form to scan.

    The backend runs regex checks to identify:

        <script> tags or event handlers (XSS)

        SQL keywords like SELECT, DROP, -- (SQLi)

    If patterns match, they are flagged and shown on the dashboard.

📸 Screenshots

    (Optional: Add screenshots or screen recordings of your dashboard and results page)

📈 Future Enhancements

    Real-time scanning of live websites using requests or Selenium.

    Integration of OWASP ZAP or Nikto for deeper scans.

    Authentication and user management for secure reporting.

    Export scan results as PDF or JSON.
