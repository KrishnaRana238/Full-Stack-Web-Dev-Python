#1. Removing Duplicates fron a list
# use case: ckleaing a contact list

contact = ["alice@gmail.com", "boy@yahoo.com", "alice@gmail.com","carol@gmail.com"]
new_contact = set(contact)  # Convert list to set to remove duplicates
print(new_contact)
