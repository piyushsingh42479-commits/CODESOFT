def chatbot(user_input):
    user_input=user_input.lower().strip()
    if "hello" in user_input or "hii" in user_input:
        return "hello! how can i help you"
    
    elif "how are you" in user_input:
        return "I'm just a ChatBot,I'm here to assist you."
    
    elif "what is your name" in user_input:
        return "I'm just a ChatBot,so i don't have a name,but you can call me ChatBot."

    elif "where are you from" in user_input:
        return "I am from the digital environment,I am here to help you"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! and have a great day!"

    else:
        return "Sorry,i don't understand that.Can you please rephrase you sentence?"
    
print("ChatBot: Hello! I'm am a Simple Chatbot,I am here to Assist you!.Type 'bye' to exit")
while True:
    user_input=input("you:")
    response=chatbot(user_input)
    print("ChatBot:",response)
    if user_input == "bye" or user_input =="exit":
        break
        print("ChatBot:",response)
        

    

    
        
        
