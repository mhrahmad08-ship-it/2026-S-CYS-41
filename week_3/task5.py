def gpa_calculator(total_subjects):
    total_marks = 0;
    total_credit_hours = 0;
    for i in range(total_subjects):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        credit_hours = int(input(f"Enter credit hours for subject {i+1}: "))
        total_marks += marks * credit_hours
        total_credit_hours += credit_hours
    gpa = total_marks / total_credit_hours
    return gpa

total_subjets = int(input("Enter the total number of subjects: "))
gpa = gpa_calculator(total_subjets)

print(f"The GPA is: {gpa}")