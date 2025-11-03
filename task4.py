# --- Vulnerability Inventory Tool ---

# Initialize sample data
vulnerabilities = [
    {"name": "SQL Injection", "severity": "Critical", "cve": "CVE-2024-1234", "status": "Open"},
    {"name": "Cross-Site Scripting", "severity": "High", "cve": "CVE-2024-5678", "status": "In Progress"},
    {"name": "Insecure Deserialization", "severity": "Medium", "cve": "-", "status": "Resolved"}
]

# Display menu
print("--- Vulnerability Inventory Tool ---")
print("1: View all vulnerabilities")
print("2: Filter vulnerabilities by severity")
print("3: Show all Open vulnerabilities")
print("4: Update vulnerability status by CVE")

choice = input("Choose an option (1-4): ")

# --- OPTION 1: View all vulnerabilities ---
if choice == "1":
    print("\n--- All Vulnerabilities ---")
    print(f"1. Name: {vulnerabilities[0]['name']}, Severity: {vulnerabilities[0]['severity']}, CVE: {vulnerabilities[0]['cve']}, Status: {vulnerabilities[0]['status']}")
    print(f"2. Name: {vulnerabilities[1]['name']}, Severity: {vulnerabilities[1]['severity']}, CVE: {vulnerabilities[1]['cve']}, Status: {vulnerabilities[1]['status']}")
    print(f"3. Name: {vulnerabilities[2]['name']}, Severity: {vulnerabilities[2]['severity']}, CVE: {vulnerabilities[2]['cve']}, Status: {vulnerabilities[2]['status']}")

# --- OPTION 2: Filter by severity ---
elif choice == "2":
    severity_filter = input("Enter severity to filter by (Critical/High/Medium/Low): ").capitalize()
    print(f"\n--- Vulnerabilities with Severity: {severity_filter} ---")

    if vulnerabilities[0]["severity"] == severity_filter:
        print(f"Name: {vulnerabilities[0]['name']}, CVE: {vulnerabilities[0]['cve']}, Status: {vulnerabilities[0]['status']}")
    elif vulnerabilities[1]["severity"] == severity_filter:
        print(f"Name: {vulnerabilities[1]['name']}, CVE: {vulnerabilities[1]['cve']}, Status: {vulnerabilities[1]['status']}")
    elif vulnerabilities[2]["severity"] == severity_filter:
        print(f"Name: {vulnerabilities[2]['name']}, CVE: {vulnerabilities[2]['cve']}, Status: {vulnerabilities[2]['status']}")
    else:
        print("No vulnerabilities match that severity.")

# --- OPTION 3: Show Open vulnerabilities ---
elif choice == "3":
    print("\n--- Open Vulnerabilities ---")
    found = False
    if vulnerabilities[0]["status"] == "Open":
        print(f"Name: {vulnerabilities[0]['name']}, CVE: {vulnerabilities[0]['cve']}, Severity: {vulnerabilities[0]['severity']}")
        found = True
    if vulnerabilities[1]["status"] == "Open":
        print(f"Name: {vulnerabilities[1]['name']}, CVE: {vulnerabilities[1]['cve']}, Severity: {vulnerabilities[1]['severity']}")
        found = True
    if vulnerabilities[2]["status"] == "Open":
        print(f"Name: {vulnerabilities[2]['name']}, CVE: {vulnerabilities[2]['cve']}, Severity: {vulnerabilities[2]['severity']}")
        found = True
    if not found:
        print("No open vulnerabilities found.")

# --- OPTION 4: Update vulnerability by CVE ---
elif choice == "4":
    cve_input = input("Enter CVE to update: ")
    new_status = input("Enter new status (Open/In Progress/Resolved): ")

    if vulnerabilities[0]["cve"] == cve_input:
        vulnerabilities[0]["status"] = new_status
        print(f"Updated {vulnerabilities[0]['name']} (CVE: {cve_input}) to status: {new_status}")
    elif vulnerabilities[1]["cve"] == cve_input:
        vulnerabilities[1]["status"] = new_status
        print(f"Updated {vulnerabilities[1]['name']} (CVE: {cve_input}) to status: {new_status}")
    elif vulnerabilities[2]["cve"] == cve_input:
        vulnerabilities[2]["status"] = new_status
        print(f"Updated {vulnerabilities[2]['name']} (CVE: {cve_input}) to status: {new_status}")
    else:
        print("CVE not found!")

# --- Invalid choice handling ---
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
