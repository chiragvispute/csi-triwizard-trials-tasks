def grading_students(grades):
    # TODO: Write logic to apply rounding rules to grades
    pass

def main():
    n = int(input("Enter number of students: "))
    grades = []
    for _ in range(n):
        grades.append(int(input("Enter grade: ")))
    
    result = grading_students(grades)
    print("Adjusted Grades:", result)

if __name__ == "__main__":
    main()
