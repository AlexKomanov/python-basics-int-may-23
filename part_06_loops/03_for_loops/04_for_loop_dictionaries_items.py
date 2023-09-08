# Loop through by Dict Keys
technology = {"Course": "python", "Fee": 4000, "Duration": "60 days"}

print(list(technology.items()))

for key, value in technology.items():
    print(key, value)

for value in technology.values():
    print(value)
