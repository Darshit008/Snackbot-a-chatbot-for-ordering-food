Directory structure
===================
backend: Contains Python FastAPI backend code
db: contains the dump of the database. you need to import this into your MySQL db by using MySQL workbench tool
dialogflow_assets: this has training phrases etc. for our intents
frontend: website code

Install these modules
======================

pip install mysql-connector
pip install "fastapi[all]"

OR just run pip install -r backend/requirements.txt to install both in one shot

To start fastapi backend server
================================
1. Go to backend directory in your command prompt
2. Run this command: uvicorn main:app --reload
Connecting to Cloudflare Tunnel
Cloudflare Tunnel allows access to the FastAPI server from the internet securely.

1. Install Cloudflare Tunnel
npm install -g cloudflared
or download it from Cloudflare

2. Login to Cloudflare

cloudflared login
3. Create a Tunnel

cloudflared tunnel create snackbot-tunnel
4. Configure the Tunnel to Forward Traffic

cloudflared tunnel route dns snackbot-tunnel myapp.example.com
5. Run the Tunnel

cloudflared tunnel run snackbot-tunnel
Your API is now accessible via https://myapp.example.com 🎉


............<h1>**WORKFLOW**<h1>......
🧠 1. User Interaction
User opens the SnackBot website.

Views food items (like Pav Bhaji, Pizza, etc.).

Adds items to the cart.

💬 2. Chatbot Integration
A Dialogflow chatbot is embedded at the bottom.

User can ask about order status, menu items, etc.

Chatbot detects intent and sends info via webhook to your backend.

🛰️ 3. FastAPI Backend
FastAPI receives chatbot's request.

It handles:

Placing orders

Calculating total price

Order tracking

Backend uses MySQL for all operations.

💽 4. MySQL Database
Stores:

orders table

order_items (item, quantity)

order_tracking (order_id, status)

Uses stored procedure to insert items.

Has a function to calculate total price.

🌐 5. HTTPS Tunnel (Cloudflare/ngrok)
FastAPI runs locally on port 8000.

A Cloudflare tunnel or ngrok exposes it to the internet (for Dialogflow webhook access).

🧪 Example Flow:
User orders “2 Samosas” via bot.

Dialogflow triggers webhook.

Webhook hits FastAPI → Inserts into DB.

DB calculates total.

FastAPI sends response → Bot replies “Your order for 2 Samosas is ₹100!”
