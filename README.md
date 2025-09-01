# HACKATHON

Project Title: BizAI - smart Operations & Finance Assistant for MSMEs

Team Members:

1.Pavithra a/p Muniandy 
2.Jaclina a/p S Jacob
3.Maneessa a/p Chandrasekaran

Problem and solution summary

1.Small and Medium Enterprises (SMEs) are the backbone of most economies, but they often face significant operational and financial management challenges. BizAI is an AI-powered, all-in-one solution that integrates business operations, financial tracking, invoicing, and client management into a single platform. Designed for ease-of-use, BizAI aims to help MSMEs run more efficiently without needing large teams or expensive software.

Technology stack used

1.Frontend: Flask (HTML/CSS/Jinja templates)
2.Backend: Python Flask
3.AI Engine: Groq API + LLaMA model for fast natural language responses
4.Database (future): Supabase/PostgreSQL for secure data storage
5.Flow: User input → Flask → AI → Dashboard update

Setup Instructions

Follow these steps to run the project locally:

1. Prerequisites

Python 3.9 or higher
pip (Python package manager)
Git (optional, for cloning repository)
Browser (Chrome/Edge/Firefox)

2. Clone or Download

Clone this repository:
git clone https://github.com/your-username/Bizai.git
Then move into the project folder:
cd Bizai.git

3. Create Virtual Environment

Create a virtual environment:
python -m venv venv
Activate it:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

4. Install Dependencies

Install the required libraries:
pip install -r requirements.txt

5. Environment Variables

Create a file named .env in the root folder and add your API keys:
GROQ_API_KEY=your_api_key_here

6. Run the Application

Run the app:
python app.py

The app will be available at:
http://127.0.0.1:5000/

7. Features to Explore

Login page – Secure entry to the dashboard.
Dashboard overview – AI insights, quick actions, and financial summary.
Task analytics – Charts for task completion, delays, and performance.
Financial analytics – Income/expense tracking, cashflow trends, and forecasts.
Invoice creator – Generate professional invoices with live preview and PDF export.
AI Chatbox Assistant – Add expenses or check sales using natural language.

Reflection on challenges and learning

1.Challenges

a.Time Limitation – Building a complete prototype with dashboard, analytics, invoicing, and AI chatbox within a short hackathon timeframe was intense. Prioritizing features was a challenge.
b.Integration of Multiple Modules – Combining Flask backend, chart visualizations, invoice generation, and AI chatbot required careful coordination. Ensuring everything worked together smoothly took extra effort.
c.API & Environment Setup – Configuring API keys (for AI assistant) and managing environment variables was tricky, especially when running on different teammates’ machines.
d.Data Handling & Visualization – Designing charts that are both accurate and easy to read was challenging, as we had to balance technical correctness with clear storytelling for users.
e.UI/UX Consistency – Making sure the dashboard looked professional while still being simple enough for demo purposes required multiple design iterations.

2. Learnings

a.Rapid Prototyping – Learned how to quickly build a working solution by focusing on core features instead of perfection.
b.Collaboration & Version Control – Improved teamwork using Git/GitHub for version management and task distribution.
c.Flask Framework – Strengthened backend development skills with Flask, routing, and integration of templates.
d.Data Visualization – Gained experience in turning raw data into meaningful insights using charts and analytics.
e.AI Integration – Learned how to connect an external AI API (Groq) into a real application, enabling natural language interaction with financial data.
f.Presentation Skills – Understood the importance of storytelling in demos — showing not just features, but also the value to end users.

