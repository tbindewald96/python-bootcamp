student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

x = student_scores[0]
for number in student_scores:
    if number > x:
        x = number

print(x)