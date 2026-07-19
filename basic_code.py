import webbrowser
import datetime

print("Jarvis Lite Started!")
print("Type 'exit' to stop.\n")

while True:
    command=input("You: ").lower()
    if command in ["hi", "hello", "hey"]:
        print("Jarvis: Hello! How can I help you?")

    elif "open youtube" in command:
        print("Jarvis: Opening YouTube...")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        print("Jarvis: Opening Google...")
        webbrowser.open("https://google.com")

    elif "time" in command:
        current_time=datetime.datetime.now().strftime("%I:%M %p")
        print("Jarvis:",current_time)

    elif command=="exit":
        print("Jarvis: Goodbye!")
        break

    else:
        print("Jarvis: Sorry, I don't understand that command.")
