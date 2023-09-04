# 1) Set the emails variable to be an empty dictionary
emails = {}

print(f"{emails = }")

# 2) Add 'ashley', 'craig', and 'elizabeth'
# to the emails dictionary without reassigning the variable.

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

print(f"{emails = }")

# 3) Remove 'craig' from the emails dictionary without reassigning the variable.

del emails['craig']

print(f"{emails = }")

# 4) Add 'dalton' to the emails dictionary without reassigning the variable.

emails['dalton'] = 'dalton@example.com'

print(f"{emails = }")

# 5) Return a list of keys from the emails dictionary as `users`

users = list(emails.keys())

print(f"{users = }")

# 6) Return a list of values from the emails dictionary as `email_list`
email_list = list(emails.values())

print(f"{email_list = }")

# 7) Return a list of tuples called `pairs`
# representing the key/value pairs in `emails`.

pairs = list(emails.items())

print(f"{pairs = }")