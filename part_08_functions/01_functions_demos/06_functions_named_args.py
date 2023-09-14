def who_are_you(name: str, age: int, role: str = "guest", experience: int = 1):
    print(f"I'm {name}, my age is {age}, my role is {role}. My experience is {experience}.")


who_are_you(role="Admin", experience=10, age=35, name="Alex")
who_are_you("Bekoni", age=10000000)
