import random
from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

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
    return render_template("dashboard.html")

@app.route("/financial")
def financial():
    return render_template("financial.html")

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
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # --- SALES FEATURE ---
    if "sales" in user_message:
        today_sales = random.randint(500, 5000)   # fake sales for today
        yesterday_sales = random.randint(500, 5000)
        reply = f"✅ Your sales today are RM{today_sales}. Yesterday you had RM{yesterday_sales}."
        return jsonify({"reply": reply})

    # --- EXPENSE FEATURE ---
    if "add my expense" in user_message:
        # Extract amount and reason
        words = user_message.split()
        amount = None
        reason = "general"

        for w in words:
            if w.isdigit():  # first number found = amount
                amount = int(w)
                break

        # Try to capture reason (e.g. last word after "for")
        if "for" in user_message:
            reason = user_message.split("for")[-1].strip()

        if amount:
            expenses.append({"amount": amount, "reason": reason})
            reply = f"✅ Expense of RM{amount} for '{reason}' added successfully."
        else:
            reply = "⚠️ Please provide a valid amount for your expense."

        return jsonify({"reply": reply})

    if "show my expenses" in user_message or "total expenses" in user_message:
        if not expenses:
            reply = "📂 You have no expenses recorded yet."
        else:
            total = sum(e["amount"] for e in expenses)
            details = ", ".join([f"RM{e['amount']} ({e['reason']})" for e in expenses])
            reply = f"📊 Your expenses: {details}. \nTotal = ${total}"
        return jsonify({"reply": reply})

    # --- DEFAULT TO AI ---
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
