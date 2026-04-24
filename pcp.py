chat_stack = []

def send_message():
    msg = input("Enter message: ")
    chat_stack.append(msg)
    print("Message stored\n")

def undo_message():
    if not chat_stack:
        print("No messages to undo\n")
    else:
        removed = chat_stack.pop()
        print(f"Removed: {removed}\n")

def view_messages():
    if not chat_stack:
        print("No messages\n")
    else:
        print("\nChat History (Latest on Top):")
        for i in range(len(chat_stack)-1, -1, -1):
            print(chat_stack[i])
        print()

# Menu
while True:
    print("1. Send Message")
    print("2. Undo Message")
    print("3. View Messages")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        send_message()
    elif choice == '2':
        undo_message()
    elif choice == '3':
        view_messages()
    elif choice == '4':
        break
    else:
        print("Invalid choice\n")