"""
Gradebook App
- list creation
- indexing
- basic list methods
"""

student_names = []
student_grades = []


def create_course():
    """Ask user for course name and return it."""
    return input("Enter course name: ").strip().title()


def add_student():
    """Add a single student and a grade."""
    name = input("Enter student name: ").strip().title()
    grade = int(input("Enter student grade(%): ").strip())

    student_names.append(name)
    student_grades.append(grade)


def update_grade():
    """Update the grade for an existing student."""
    # Ask which student
    name = input("Enter student to update: ").strip().title()
    # Search for student and ask for new grade
    if name in student_names:
        index = student_names.index(name)  # Gets the index of that name
        new_grade = int(input("Enter new grade(%): ").strip())
        student_grades[index] = new_grade
        print("Grade updated.")
    else:
        print("Student not found.")


def remove_student():
    """Remove a student and their grade"""
    # Ask for student name for removal
    name = input("Enter student name to remove: ").strip().title()

    # Search for student
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)  # Get rid of that student
        student_grades.pop(index)  # Get rid of that student's grade
    else:
        print("Student not found.")


def show_roster():
    """Display all students and grades."""
    # Do something if there are no students
    if not student_names:  # If there is nothing in student_names
        print("No students in course.")
        return
    # Loop through names list and print each student name with their grade
    print("\nClass Roster:")
    for i in range(len(student_names)):
        print(student_names[i], "-", student_grades[i])


def show_statistics():
    """Display class stats."""
    # Do something if there are no students.
    if not student_names:
        print("There are no students recorded!")
        return
    # Calculate mean average
    average = sum(student_grades) / len(student_grades)
    # Show mean, maximum, and minimum grades
    print("\nClass Statistics:")
    print("Average:", round(average,2))
    print("Highest grade:", max(student_grades))
    print("Lowest grade:", min(student_grades))


def main():
    """Main program loop"""

    # Create course
    course = create_course()
    print(f"\nWelcome to {course}!") # Welcome user to course
    
    while True:
        # Show options
        print("\n1 - Add Student")
        print("2 - Update grade")
        print("3 - Remove Student")
        print("4 - Show Roster")
        print("5 - Show Statistics")
        print("0 - Exit")
        # Ask user what option they want
        choice = input("Choose an option: ").strip()
        # Add student
        if choice == "1":
            add_student()
        # Update grade
        elif choice == "2":
            update_grade()
        # Remove student
        elif choice == "3":
            remove_student()
        # Show roster
        elif choice == "4":
            show_roster()
        # Show statistics
        elif choice == "5":
            show_statistics()
        # Exit
        elif choice == "0":
            break
        else:
            print("Please enter your choice.")


if __name__ == "__main__":
    main()