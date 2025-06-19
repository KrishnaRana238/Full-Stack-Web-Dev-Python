# 4. Checking for Membership
#use cases: check if a user has already registered

registered_users = {"alice", "bob", "carol"}

check_user = "dave"

print(f"Is '{check_user}' registered? {check_user in registered_users}")