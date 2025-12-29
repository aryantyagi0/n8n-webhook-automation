import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get webhook URL from .env
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("N8N_WEBHOOK_URL not found in environment variables")

response = requests.post(
    WEBHOOK_URL,
    json={
        "action": "create_ticket",
        "name": "Aryan",
        "email": "at9120140@gmail.com",
        "message": "My order is delayed"
    }
)

print("Status Code:", response.status_code)
