# score_1, score_2, score_3, score_4, score_5 = map(int, input("Enter 5 scores: ").split())

# Stage 1 - Read the whole value:
whole_input = input("Enter 5 scores: ")
print("whole_input", whole_input)

# Stage 2 - Split the whole value:
whole_input_after_split = whole_input.split()
print("whole_input_split", whole_input_after_split)
print("type(whole_input_split)", type(whole_input_after_split))

# Stage 3 - convert any value and store the value (using loop with iterations)
score_1 = int(whole_input_after_split[0])
score_2 = int(whole_input_after_split[1])
score_3 = int(whole_input_after_split[2])
score_4 = int(whole_input_after_split[3])
score_5 = int(whole_input_after_split[4])

print(score_1 + score_2 + score_3 + score_4 + score_5)
