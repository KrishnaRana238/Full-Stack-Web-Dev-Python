# Problem: Detecting Duplicate Email Addresses in a Signup System
# Scenario:
# You are managing a web application that allows users to sign up with their email addresses.
# You want to ensure that each user registers only once using a unique email address.
# You receive a list of new signups and need to find out which email addresses are duplicates.

# (i.e. have already signed up before).
# Solution

# def detect_duplicate_emails(signup_list):
#     seen_emails = set()  # Set to store unique email addresses
#     duplicates = set()  # Set to store duplicate email addresses
#     if not signup_list:
#         return duplicates
#     for email in signup_list:
#         if email in seen_emails:
#             duplicates.add(email)
#         else:
#             seen_emails.add(email)
#     return duplicates
# print(detect_duplicate_emails(signup_list=["bob@gmail.com","alice@gmail.com","bol@gmail.com","bob@gmail.com"]))


exits_email= {"alice@example.com","bob@example.com"}
signup_list = [ "alice@example.com","bob@example.com","charlie@example.com","alice@example.com", "dave@example.com","BOB@example.com",   "bob@example.com"]

# def detect_duplicate_emails(email_list):
#     return list(set(email for email in email_list if email_list.count(email) > 1))

# duplicate = detect_duplicate_emails(signup_list)
# print(f"Duplicate email addresses: {duplicate}")

new_signup_List = set(signup_list)
duplicates = exits_email & new_signup_List
unique_emails = new_signup_List - duplicates
print(f"Duplicate email addresses: {duplicates}")
print(f"Unique email addresses: {unique_emails}")