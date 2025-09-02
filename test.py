""""
student_name = "Alice"
midterm = 85
final = 92
homework = 88

total_grade = (midterm * 0.3) + (final * 0.4) + (homework * 0.3)
print(f"{student_name} total grade = {total_grade}")
"""


def check_grade(score):
    if score >=80:
        return "very good"
    elif score >=70:
        return "good"
    elif score >=60:
        return "normal"
    else:
        return "should be improved"
test_score =[85, 75, 65, 55]
for s in test_score:
    print(f"Score : {s} = {check_grade(s)}")

""""
scores = [78, 85, 92, 67, 88, 95, 73, 84]
max_score = max(scores)
min_score = min(scores)
avg_score = sum(scores)/len(scores)
count_above_80 = len([s for s in scores if s > 80])
print("Max score is ", max_score)
print("Min score is ", min_score)
print("Average score is ", avg_score)
print("People have score more than 80 is ", count_above_80)
"""