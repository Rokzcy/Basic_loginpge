# Prompt user for name and password
username_prompt = "Please type in your name: "
password_prompt = "Please type in your password: "

# Get input from the user
entered_username = input(username_prompt)
entered_password = input(password_prompt)

# Hardcoded credentials
correct_username = "mrrty"
correct_password = "1534"  # keeping as string for input comparison

# Check credentials
if entered_username == correct_username and entered_password == correct_password:
    print("Access granted")
else:
    print("Access denied")