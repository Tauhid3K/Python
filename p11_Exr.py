email = input("Enter your email address: ")

# find the index of "@" in the email
index = email.index("@")

# Finding only user name and domain from the email
username = email[:index]
domain = email[index +1 :]

print(f"Username: \"{username}\" and domain: \"{domain}\" ") 