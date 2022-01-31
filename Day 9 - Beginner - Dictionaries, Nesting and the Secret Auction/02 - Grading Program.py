#You have access to a database of student_scores in the format of a dictionary. The
#keys in student_scores are the names of the students and the values are their exam scores.

#Write a program that converts their scores to grades.
#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

#Remember that looping through a Dictionary will only give you the keys and not the values.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for name in student_scores:
    if student_scores[name] >=  91:
        student_grades[name] = "Outstanding"
    elif student_scores[name] >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"
        
print(student_grades)