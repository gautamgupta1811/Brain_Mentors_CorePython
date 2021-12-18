hello_intent = ["hello", "heyy", "good morning", "good afternoon", "hi", "hii"]
bye_intent = ["bye", "see you" ,"talk to you later", "ttyl", "soon", "later"]

while True:
    msg = input("Enter your message: ")
    if msg.lower() in hello_intent:
        print("Heyy there")
    elif msg.lower() in bye_intent:
        print("See you around")
        break
    else:
        print("I don't understand")
