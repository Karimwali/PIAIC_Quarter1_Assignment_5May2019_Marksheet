# requirements of this assignment
# get 6 input from users which ask users about the marks obtained in each subject
# return the overall grade, percentage and marksheet of the user 


#defining all variables 
user_marks = {"Sindhi":0, "English":0, "Chemistry":0, "ComputerScience": 0, "PakistanStudies": 0} 
total_acheived_marks = 0
total_marks = 0
subject_count = 0
grade = ""


# getting user input
student_name = input("Please enter your name: ")

print("Please print your marks acheived in the following subjects;")

for i in user_marks:
    while True:  # validation to ensure that user enter only valid numbers 
        try:
            user_marks[i] = float(input("{subject} = ".format(subject = i)))
            if user_marks[i] > 100:
                raise ValueError
            break
        except ValueError: #validation to ensure that user not enter marks above 100
            print("Marks in one subject can not be greater than 100")
        except: # validation to ensure that user enter only valid numbers 
            print("You have an entered an incorrent number.")

# calculating total marks acheived and the number of subjects
for key, value in user_marks.items():
    #print(key, value)
    total_acheived_marks = total_acheived_marks + value
    subject_count = subject_count + 1

# calculating average marks
average_marks = total_acheived_marks / subject_count

# calculating grades 
if average_marks >= 90:
    grade = "A+" 
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "Failed"

print("") # line break

# printing a response to user
if average_marks >= 50:
    print(
        "Congratulations {student_name}, you have passed your board exams and have acheived grade '{grade}'. You have obtained total {total_acheived_marks} out of {total_available_marks} and therefore your overall percentage is {average_marks}%".format(
            student_name = student_name, 
            grade = grade, 
            total_acheived_marks = int(total_acheived_marks), 
            total_available_marks = subject_count * 100,
            average_marks = average_marks
            )
    )
else:
    print(
        "Sorry {student_name}, you have failed  your board exams.".format(student_name = student_name)
    )

