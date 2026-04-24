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


def view_stack():
    if not attack_stack:
        print(" No attack records\n")
        return

    print("\n Current Attack Stack (Latest on Top):\n")
    for i in range(len(attack_stack)-1, -1, -1):
        r = attack_stack[i]
        print(f"{r['Action']} | {r['IP']} | {r['Severity']} | {r['Time']}")
    print()


def peek_latest():
    if not attack_stack:
        print("No recent attack\n")
        return

    r = attack_stack[-1]
    print("\n Most Recent Attack:")
    print(f"{r['Action']} from {r['IP']} at {r['Time']} ({r['Severity']})\n")


def main():
    while True:
        print("====== CYBER ATTACK TRACE SYSTEM ======")
        print("1. Log Attack")
        print("2. Trace Latest Attack (Undo)")
        print("3. View All Logs")
        print("4. Peek Latest Attack")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            log_attack()
        elif choice == '2':
            trace_latest_attack()
        elif choice == '3':
            view_stack()
        elif choice == '4':
            peek_latest()
        elif choice == '5':
            print("Exiting System...")
            break
        else:
            print(" Invalid choice\n")


main()