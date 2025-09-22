import re
def chatbot():
    print("Welcome to the customer support chatbot!")
    print("How may I help you today?")
    print("Type 'exit' anytime to end the chat.\n")


    responses = {
        r"(price|cost).*product":"Our product range from 10rs to 1000rs depending upon the items.",
        r"(return|refund).*policy":"You can return items within 7 days for a full refund.",
        r"(track|status).*order":"Please provide your orderID to track your order.",
        r"(payment|pay).*methods":"We accept debit card, credit cards and UPI payments.",
        r"(support|help).*email":"You can email support@company.com for detailed assistance.",

    }

    while True:
        user_input=input("You: ").lower().strip()
        if user_input in ["exit","quit","bye"]:
            print("Chatbot: Thank you for visiting. Have a great day!")
            break
        matched = False
        for pattern, reply in responses.items():
            if re.search(pattern,user_input):
                print("chatbot: ",reply)
                matched = True
                break
        if not matched:
            print("chatbot: I'm sorry, I don't have information on that, please contact support@comapany.com")


if __name__ == "__main__":
    chatbot()