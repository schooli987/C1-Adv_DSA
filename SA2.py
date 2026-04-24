attack_stack = []

def log_attack():
    ip = input("Enter Attacker IP: ")
    action = input("Enter Action (e.g., Login, Malware, Data Theft): ")
    severity = input("Enter Severity (Low/Medium/High): ")
    time = input("Enter Time (e.g., 10:45 PM): ")

    record = {
        "IP": ip,
        "Action": action,
        "Severity": severity,
        "Time": time
    }

    attack_stack.append(record)
    print("Attack Logged Successfully\n")


def trace_latest_attack():
    if not attack_stack:
        print("⚠️ No attacks to trace\n")
        return

    record = attack_stack.pop()
    print("\n🔍 Tracing Latest Attack Step:")
    print(f"IP: {record['IP']}")
    print(f"Action: {record['Action']}")
    print(f"Severity: {record['Severity']}")
    print(f"Time: {record['Time']}\n")




def main():
    while True:
        print("====== CYBER ATTACK TRACE SYSTEM ======")
        print("1. Log Attack")
        print("2. Trace Latest Attack (Undo)")
    
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            log_attack()
        elif choice == '2':
            trace_latest_attack()
       
        elif choice == '5':
            print("Exiting System...")
            break
        else:
            print(" Invalid choice\n")


main()