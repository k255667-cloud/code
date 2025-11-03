# Simple Name Classification Program

# Ask user for 4 names in one line, separated by commas
names_input = input("Enter 4 student names separated by commas: ")

# Split and strip spaces
names = [name.strip() for name in names_input.split(",")]

# Initialize category lists
a_names = []
b_names = []
c_names = []
others = []

# Classify each of the 4 names using if-elif-else (no loops)
if names[0][0].lower() == "a":
    a_names.append(names[0])
elif names[0][0].lower() == "b":
    b_names.append(names[0])
elif names[0][0].lower() == "c":
    c_names.append(names[0])
else:
    others.append(names[0])

if names[1][0].lower() == "a":
    a_names.append(names[1])
elif names[1][0].lower() == "b":
    b_names.append(names[1])
elif names[1][0].lower() == "c":
    c_names.append(names[1])
else:
    others.append(names[1])

if names[2][0].lower() == "a":
    a_names.append(names[2])
elif names[2][0].lower() == "b":
    b_names.append(names[2])
elif names[2][0].lower() == "c":
    c_names.append(names[2])
else:
    others.append(names[2])

if names[3][0].lower() == "a":
    a_names.append(names[3])
elif names[3][0].lower() == "b":
    b_names.append(names[3])
elif names[3][0].lower() == "c":
    c_names.append(names[3])
else:
    others.append(names[3])

# Print results
print("\n--- Classification Results ---")
print(f"A names: {a_names} (Total: {len(a_names)})")
print(f"B names: {b_names} (Total: {len(b_names)})")
print(f"C names: {c_names} (Total: {len(c_names)})")
print(f"Others: {others} (Total: {len(others)})")
