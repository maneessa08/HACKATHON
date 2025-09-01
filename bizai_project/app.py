import random
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from groq import Groq
import os
import re


app = Flask(__name__)
app.secret_key = "b7f3a2c1e9d4g8h5j0k6l2m9p4q7r1s8"  


# --- Load API Key safely ---
api_key = os.getenv("GROQ_API_KEY")
if not api_key:  # fallback to file
    try:
        with open("api_key.txt", "r", encoding="utf-8") as f:
            api_key = f.read().strip().replace('"', '').replace("'", "")
        os.environ["GROQ_API_KEY"] = api_key  # set for SDK compatibility
    except FileNotFoundError:
        raise RuntimeError("❌ No API key found. Please set GROQ_API_KEY or create api_key.txt")

# Initialize Groq client
client = Groq(api_key=api_key)

# Store expenses in memory (for demo purpose)
expenses = []

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form.get("username", "Guest")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/financial")
def financial():
    return render_template("financial.html")

@app.route("/reminder1")
def reminder1():
    return render_template("reminder1.html")

@app.route("/invoice")
def invoice():
    return render_template("invoice.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/signout")
def signout():
    return render_template("signout.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = str(data.get("message", "")).strip()
    msg_lower = user_message.lower()

    # --- GREETING FEATURE ---
    if msg_lower in ["hi", "hello", "hey", "hye"]:
        reply = "👋 Hi there! How can I help you today?"
        return jsonify({"reply": reply})

    # --- SALES FEATURE ---
    if "sales" in msg_lower:
        today_sales = random.randint(500, 5000)   # fake sales for today
        yesterday_sales = random.randint(500, 5000)
        reply = f"✅ Your sales today are RM{today_sales}. Yesterday you had RM{yesterday_sales}."
        return jsonify({"reply": reply})

    # --- EXPENSE FEATURE ---
    if "add my expense" in msg_lower:
        # Look for numbers like "200", "200.50", "RM200"
        m = re.search(r'(?i)\brm?\s*([0-9]+(?:\.[0-9]{1,2})?)\b', user_message)
        if not m:
            m = re.search(r'\b([0-9]+(?:\.[0-9]{1,2})?)\b', user_message)
        amount = float(m.group(1)) if m else None

        # Reason after "for"
        reason = "general"
        m2 = re.search(r'(?i)\bfor\s+(.+)$', user_message)
        if m2:
            reason = m2.group(1).strip(" .")

        if amount is not None:
            expenses.append({"amount": amount, "reason": reason})
            reply = f"✅ Expense of RM{amount:,.2f} for '{reason}' added successfully."
        else:
            reply = "⚠️ Please provide a valid amount, e.g. 'add my expense RM25 for lunch'."
        return jsonify({"reply": reply})

    if "show my expenses" in msg_lower or "total expenses" in msg_lower:
        if not expenses:
            reply = "📂 You have no expenses recorded yet."
        else:
            total = sum(float(e["amount"]) for e in expenses)
            details = ", ".join([f"RM{float(e['amount']):,.2f} ({e['reason']})" for e in expenses])
            reply = f"📊 Your expenses: {details}.\nTotal = RM{total:,.2f}"
        return jsonify({"reply": reply})

    # --- DEFAULT TO AI ---
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = "❌ Sorry, I couldn't reach the AI service. Please try again later."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
