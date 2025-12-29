import requests

requests.post(
    "https://aryan99.app.n8n.cloud/webhook-test/support-agentf",
    json={
        "action": "create_ticket",
        "name": "Aryan",
        "email": "at9120140@gmail.com",
        "message": "My order is delayed"
    }
)
