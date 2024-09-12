# Create a list of test scores for a student.
test_scores = [80,96,92,100,89]
score_sum = sum(test_scores)
length = len(test_scores)

# Use floor division to calculate the average score.
average = score_sum // length

# Use comparison operators to determine the grade based on the average score.
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 80:
    grade = "C"
elif average >= 70:
    grade = "D"
elif average >= 60:
    grade = "E"
else:
    grade = "F"

# Use assignment operators to update the student's grade.
bonus = score_sum % 10
if bonus >= 5:
    grade += "+"

# Use membership operators to check if a specific score exists in the list of scores.
specific_score = 70
if specific_score in test_scores:
    print(f"Specific score {specific_score} is in test scores")
else:
    print(f"Specific score {specific_score} is not in test scores")

# Use identity operators to compare objects.
compare_test_scores = test_scores
if test_scores is compare_test_scores:
    print("Comapre test scores and test scores are the same object")
else:
    print("Comapre test scores and test scores are not the same object")

# Use bitwise operators to perform bitwise operations on the scores.
bitwise_score = test_scores[0] & test_scores[1]
print(f"Bitwise AND of the first two scores: {bitwise_score}")

# Display the student's grade
print(f"The student's average score is {average} and their grade is {grade}.")



