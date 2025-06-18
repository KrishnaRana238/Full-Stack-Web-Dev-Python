# Task 3 Guest like for a party
# create a list of guests
# add new guest
# check if a guest is on the list
# remove a guest from who cancels
    
    
    
guest_list = []

num = int(input("How many guests do you want to add? "))
for i in range(num):
    guest = input(f"Enter the name of guest {i + 1}: ")
    guest_list.append(guest)   
print("Current Guest List:", guest_list)

new_guest = input("Enter the name of the new guest to add: ")
if new_guest not in guest_list:
    guest_list.append(new_guest)
    print(f"{new_guest} has been added to the guest list.")
else:
    print(f"{new_guest} is already on the guest list.")
    
check_guest = input("Enter the name of the guest to check: ")
if check_guest in guest_list:
    print(f"{check_guest} is on the guest list.")
else:
    print(f"{check_guest} is not on the guest list.")
    
remove_guest = input("Enter the name of the guest to remove: ")
if remove_guest in guest_list:
    guest_list.remove(remove_guest)
    print(f"{remove_guest} has been removed from the guest list.")

print("Updated Guest List:", guest_list)