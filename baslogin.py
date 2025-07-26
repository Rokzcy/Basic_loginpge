# Stored credentials (for demonstration)
correct_username = "marty"
correct_password = "1234"

# Set maximum login attempts
max_attempts = 5
attempts = 0

# Login loop
while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("✅ Access granted. Welcome,", username + "!")
        break
    else:
        attempts += 1
        print("❌ Incorrect username or password. Attempts left:", max_attempts - attempts)

# Lockout after max attempts
if attempts == max_attempts:
    print("🔒 Too many failed attempts. Access denied.")
