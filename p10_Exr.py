user_name = input("Enter your user name: ")

if len(user_name) > 12:
    print("User name should not exceed 12 characters.")
elif not user_name.find(" ") == -1:
    print("User name should not contain spaces.")
elif not user_name.isalpha():
    print("User name should not contain digits.")
else:
    print(f"User name {user_name} is valid.")
