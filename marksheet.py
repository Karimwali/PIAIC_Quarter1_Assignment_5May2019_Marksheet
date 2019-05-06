# get 6 input from users which ask users about the marks obtained in each subject
# return the overall grade, percentage and marksheet of the user 


# getting user input
user_marks = {"Sindhi":0, "English":0, "Chemistry":0, "ComputerScience": 0} 
total_acheived_marks = 0
total_marks = 0
subject_count = 0

print("Please print your marks acheived in the following subjects;")

for i in user_marks:
    while True:  # validation to ensure that user enter only valid numbers 
        try:
            user_marks[i] = float(input("{subject} = ".format(subject = i)))
            if user_marks[i] > 100:
                raise ValueError
            break
        except ValueError:
            print("Marks in one subject can not be greater than 100")
        except:
            print("You have an entered an incorrent number.")

print("")
print("You Marksheet Scores")
for key, value in user_marks.items():
    #print(key, value)
    total_acheived_marks = total_acheived_marks + value
    subject_count = subject_count + 1

average_marks = total_acheived_marks / subject_count


print("Total marks = {marks}".format(marks = total_acheived_marks))

print("Average marks (in percentage) = {marks} %".format(marks = average_marks))

#Grades working
if average_marks >= 90:
    print("Grade A+")
elif average_marks >= 70:
    print("Grade A")
elif average_marks >= 60:
    print("Grade B")
elif average_marks >= 50:
    print("Grade C")
else:
    print("Failed!!")
