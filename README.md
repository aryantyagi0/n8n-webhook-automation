
# n8n Webhook Automation (Agentic Support Flow)

This project demonstrates an **agentic customer support automation** using Python and n8n.
It sends structured customer data to an n8n webhook, where workflows such as **automatic email sending** or **ticket creation** are executed.

---

##  Project Overview

The system simulates a customer support agent by:
- Receiving customer messages
- Sending structured data (action, name, email, message)
- Triggering automated workflows in n8n via webhook

This project follows **best practices** by keeping sensitive configuration values in environment variables.

---

## 🔁 Workflow

Python Script
↓
n8n Webhook
↓
Conditional Logic (IF node)
↓
Automatic Email / Ticket Creation



---

##  Technologies Used

- **Python**
- **requests** – HTTP requests
- **python-dotenv** – Environment variable management
- **n8n** – Workflow automation

---

##  How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/aryantyagi0/n8n-webhook-automation.git
cd n8n-webhook-automation
2️⃣ Create a virtual environment (optional)
bash
Copy code
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Install dependencies

pip install requests
langgraph
langchain-openai
openai
python-dotenv


pip install requests python-dotenv
4️⃣ Set environment variables
Create a .env file:

env
Copy code
N8N_WEBHOOK_URL=your_n8n_webhook_url_here
 .env is ignored using .gitignore for security.

 Run the script
bash
Copy code
python webhook.py
 Example Payload Sent to n8n
json
Copy code
{
  "action": "create_ticket",
  "name": "Aryan",
  "email": "user@example.com",
  "message": "My order is delayed"
}
 Security Best Practices
Sensitive data stored in .env

.env excluded from GitHub using .gitignore

.env.example can be used for reference

 Use Cases
Automated customer support workflows

Conditional email notifications

Ticket creation systems

Event-driven automation

 Conclusion
This project shows how Python scripts can integrate with n8n webhooks to build reliable, event-driven automation systems with clean separation of logic and configuration.

 Author
Aryan Tyagi











