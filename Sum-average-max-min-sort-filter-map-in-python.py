student_data = [
   {"id": "012202100001", "name": "John Doe", "score": 90.7},
   {"id": "012202100002", "name": "Jack Smith", "score": 80},
   {"id": "012202100003", "name": "Randall Lu", "score": 70.65},
   {"id": "012202100004", "name": "Samantha Arden", "score": 65},
   {"id": "012202100005", "name": "Abby Johnson", "score": 60},
   {"id": "012202100006", "name": "Rick Martin", "score": 55},
   {"id": "012202100007", "name": "Maria Park", "score": 78.5},
   {"id": "012202100008", "name": "Rene Christine", "score": 89.5},
   {"id": "012202100009", "name": "Christie Alexander", "score": 100},
   {"id": "012202100010", "name": "David Holler", "score": 77},
]

print("***Question 1***")

#Total
total_scores = sum(data["score"] for data in student_data)
print("Total:", total_scores)

#Average
average_score = total_scores / len(student_data)
print("Average:", average_score)

#Maximum data
max_score = max(data['score'] for data in student_data)
students_with_max_score = [data for data in student_data if data['score'] == max_score]

for data in students_with_max_score:
    print("Maximum data:", data['id'], data['name'], data['score'])

#Minimum data
min_score = min(data['score'] for data in student_data)
students_with_min_score = [data for data in student_data if data['score'] == min_score]

for data in students_with_min_score:
    print("Minimum data:", data['id'], data['name'], data['score'])

print()
print("***Question 2***")

# Sorted score
sortedscore = sorted(student_data, key=lambda data: data["score"])
print("Sorted by Score:")
for data in sortedscore:
    print("Score:", data["score"])
    print()

# Sorted name
sortedname = sorted(student_data, key=lambda data: data["name"])
print("Sorted by Name:")
for data in sortedname:
    print("Name:", data["name"])

print()
print("***Question 3***")

def get_data_higher_than_equal(data, min_score):
    filtered_data = [student for student in data if student['score'] >= min_score]
    return filtered_data

min_score = 80  # example
result = get_data_higher_than_equal(student_data, min_score)
print(result)

print()
print("***Question 4***")

def letter_of_grade(score):
    if 85 <= score <= 100:
        return "A"
    elif 70 <= score < 85:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif 55 <= score < 60:
        return "D"
    elif 0 <= score < 55:
        return "E"
    else:
        return "Invalid"

def get_letter_grade(student_data):
    lettergrade = []
    for student in student_data:
        grade = letter_of_grade(student['score'])
        lettergrade.append(grade)
    return lettergrade


result = get_letter_grade(student_data)
print(result)

print()
print("***Question 5***")

def grading_count(grades):
    count_A = grades.count('A')
    count_B = grades.count('B')
    count_C = grades.count('C')
    count_D = grades.count('D')
    count_E = grades.count('E')
    return count_A, count_B, count_C, count_D, count_E

result = get_letter_grade(student_data)

count_A, count_B, count_C, count_D, count_E = grading_count(result)

print("A =", count_A)
print("B =", count_B)
print("C =", count_C)
print("D =", count_D)
print("E =", count_E)