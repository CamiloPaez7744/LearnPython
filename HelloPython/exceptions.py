age_str = input("Enter your age: ")

try:
    age = int(age_str)
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"You are {age} years old.")
except ValueError as e:
    if str(e) == "Age cannot be negative.":
        print("Error: Age cannot be negative.")
    else:
        print("Invalid input: Please enter a valid non-negative integer for age.")