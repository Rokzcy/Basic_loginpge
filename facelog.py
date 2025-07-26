# Facebook-style Login System

# Dictionary of users and their respective passwords
user_credentials = {
    "james": "pass123",
    "favour": "JOSEPH",
    "jennifer": "home456",
    "make": "strongpass",
    "amara": "helloWorld"
}

# Welcome screen
print("=" * 40)
print(" " * 10 + "Welcome to Facebook")
print("=" * 40)

# Allow 3 login attempts
MAX_ATTEMPTS = 3
attempts = 0
authenticated = False

while attempts < MAX_ATTEMPTS:
    print(f"\nLogin Attempt {attempts + 1} of {MAX_ATTEMPTS}")

    # Get user input
    username_input = input("Enter your username: ").lower().strip()
    password_input = input("Enter your password: ").strip()

    # Check if username exists
    if username_input in user_credentials:
        # Check if password matches
        if password_input == user_credentials[username_input]:
            print("\n✅ Login successful!")
            print(f"Welcome, {username_input.capitalize()}!")
            authenticated = True
            break
        else:
            print("❌ Incorrect password.")
    else:
        print("❌ Username not found.")

    attempts += 1

# Final check after loop
if not authenticated:
    print("\n🚫 Too many failed login attempts.")
    print("Please try again later or reset your password.")
