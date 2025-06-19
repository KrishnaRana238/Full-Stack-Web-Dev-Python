# 1. Contact Book Application
# Task: Store and retrive contact information (name, phone number, email.
#
contacts = {
     "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
     "Bob": {"phone": "987-654-3210", "email": "bob@example.com"}    
}

set_contact = set(contacts.keys())
for i in contacts.items():
    print("Contact Name:", i[0])
    print("Phone Number:", i[1]["phone"])
    print("Email:", i[1]["email"])
    