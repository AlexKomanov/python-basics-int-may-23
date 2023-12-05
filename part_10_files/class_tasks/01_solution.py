def create_file_with_numbers(n):
    file_name = f"range_{n}.txt"

    with open(file_name, 'w') as file:
        for number in range(1, n + 1):
            file.write(f"{number}\n")

    print(f"File '{file_name}' created successfully.")


# Example usage:
create_file_with_numbers(5)
