#email validator  function to check if an email is valid or not, @ and .

email = input("Enter an email address: ")

def email_validator(email):
    if "@" not in email or "." not in email:
        return "Invalid email address. It must contain '@' and '.'"
    if email.count("@") != 1:
        return "Invalid email address. It must contain exactly one '@' symbol."
    if email.index("@") == 0 or email.index("@") == len(email) - 1:
        return "Invalid email address. '@' cannot be at the start or end."
    if email.index(".") == 0 or email.index(".") == len(email) - 1:
        return "Invalid email address. '.' cannot be at the start or end."
    if email.index(".") < email.index("@"):
        return "Invalid email address. '.' must come after '@'."
    return "Valid email address."
print(email_validator(email)) 