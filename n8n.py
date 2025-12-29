from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
import requests
import os
from dotenv import load_dotenv

# -------------------------
# LOAD ENV VARIABLES
# -------------------------
load_dotenv()

# -------------------------
# LLM CONFIG
# -------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# -------------------------
# STATE DEFINITION
# -------------------------
class SupportState(TypedDict):
    user_message: str
    intent: str
    action: str
    name: str
    email: str

# -------------------------
# NODE 1: INTENT DETECTION
# -------------------------
def detect_intent(state: SupportState):
    prompt = f"""
    Classify the intent of this message into one of these:
    - complaint
    - general_query
    - feedback

    Message: {state['user_message']}
    """

    intent = llm.invoke(prompt).content.lower()
    state["intent"] = intent
    return state

# -------------------------
# NODE 2: DECIDE ACTION
# -------------------------
def decide_action(state: SupportState):
    if "complaint" in state["intent"]:
        state["action"] = "create_ticket"
    elif "feedback" in state["intent"]:
        state["action"] = "send_thank_you"
    else:
        state["action"] = "auto_reply"

    return state

# -------------------------
# NODE 3: CALL n8n WEBHOOK
# -------------------------
def call_n8n(state: SupportState):
    n8n_webhook_url = os.getenv("N8N_WEBHOOK_URL")

    if not state.get("email"):
        print(" No email found. Skipping n8n call.")
        return state

    payload = {
        "action": state["action"],
        "message": state["user_message"],
        "name": state["name"],
        "email": state["email"]
    }

    response = requests.post(n8n_webhook_url, json=payload)

    print(" n8n Response Status:", response.status_code)
    return state

# -------------------------
# LANGGRAPH SETUP
# -------------------------
graph = StateGraph(SupportState)

graph.add_node("intent_detection", detect_intent)
graph.add_node("decision", decide_action)
graph.add_node("execute_action", call_n8n)

graph.set_entry_point("intent_detection")

graph.add_edge("intent_detection", "decision")
graph.add_edge("decision", "execute_action")
graph.add_edge("execute_action", END)

app = graph.compile()

# -------------------------
# RUN APPLICATION
# -------------------------
if __name__ == "__main__":
    user_message = input("Enter customer message: ")
    name = input("Enter user name: ")
    email = input("Enter user email: ")

    result = app.invoke({
        "user_message": user_message,
        "name": name,
        "email": email
    })

    print("\nFinal State:")
    print(result)
