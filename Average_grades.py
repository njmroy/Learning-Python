# Get grades function definition
# Generates list of 5 floats from user to represent grades
def get_grades():
    grades = []
    for i in range(0, 5, 1):
        grades.append(float(input("Enter grade number " + str(i + 1) + ": ")))
    return grades


# Calculate average function definition
# Takes list as input, outputs average as float
def calc_average(grades):
    total = 0
    for i in grades:
        total += i
    return total / len(grades)


# Determine grade function definition
# Converts grades to letters based on value
# Returns list of alpha grades
def determine_grade(grades):
    grade_list = []
    for grade in grades:
        if 90 <= grade <= 100:
            grade_list.append("A")
        elif 80 <= grade <= 89:
            grade_list.append("B")
        elif 70 <= grade <= 79:
            grade_list.append("C")
        elif 60 <= grade <= 69:
            grade_list.append("D")
        else:
            grade_list.append("F")
    return grade_list


# Main function definition
def main():
    # Get grades from user
    grades = get_grades()

    # Get average, add to grade list
    grades.append(calc_average(grades))

    # Convert number grades to letter grades
    alpha = determine_grade(grades)

    # Output each grade number and letter grade, including final average
    for i in range(0, len(alpha), 1):
        if i == 5:
            print("Average is " + str(grades[i]) + ", which is equivalent to: " + alpha[i])
        else:
            print("Grade " + str(grades[i]) + " is equivalent to: " + alpha[i])


# Main function call
main()
