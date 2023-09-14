original_array = [2, 5, 8, 10, 25, -5, 200]

filtered_array = list(filter(lambda x: x > 8, original_array))

print(filtered_array)


server_json = [
    {'task_name': 'Learn Python', 'status': "In Progress"},
    {'task_name': 'Learn Java', 'status': "Done"},
    {'task_name': 'Learn TypeScript', 'status': "Done"},
    {'task_name': 'Learn GO', 'status': "New"},
]

filtered_json = list(filter(lambda x: x['status'] == 'In Progress' or x['status'] == 'New', server_json))

print(filtered_json)
