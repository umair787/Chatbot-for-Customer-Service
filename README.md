**Project Setup**

Make a folder:

```
customer_service_chatbot/
└─ chatbot.py
```

No extra installations are required for the basic version—just Python (≥3.7).

Python Code – **chatbot.py**

Simple Rule-Based Chatbot


**How it Works**

* Uses **regular expressions (`re`)** to match user messages with patterns like “price”, “refund”, or “track order”.
* If a match is found, it replies with a predefined response.
* If no match is found, it gives a default “contact support” reply.

---

**Run the Chatbot**

In the terminal:

```bash
python chatbot.py
```

Example session:

```
Welcome to the Customer Service Chatbot!
Type 'exit' anytime to end the chat.

You: hello
Chatbot: Hello! How can I help you today?
You: what is your refund policy
Chatbot: You can return items within 30 days for a full refund.
You: bye
Chatbot: Thank you for visiting. Have a great day!
```

