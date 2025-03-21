
import winsound

def get_final_grade(average):
    if 90 <= average <= 100:
        return 'A', '- Excellent'
    elif 80 <= average < 90:
        return 'B', '- Good'
    elif 70 <= average < 80:
        return 'C', '- Satisfactory'
    elif 65 <= average < 70:
        return 'D', 'Passing - Needs work'
    else:
        return 'F', '- Failing'

def main():
    print("Welcome, Teacher!")
    winsound.Beep(200, 20)

    while True:
        student_name = input("\nEnter the student's name: ").strip()

        # Grade entry loop
        grades = []
        print("Enter grades for {}. Type -1 to finish entering grades.".format(student_name))

        while True:
            try:
                grade_input = input("Enter grade (0-100) or -1 to finish: ")
                winsound.Beep(400, 200)
                grade = int(grade_input)

                if grade == -1:
                    break
                elif 0 <= grade <= 100:
                    grades.append(grade)
                else:
                    print("Invalid grade. Please enter a number between 0 and 100, or -1 to finish.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if grades:
            average = sum(grades) / len(grades)
            letter_grade, description = get_final_grade(average)

            print("\n--- Student Report ---")
            print(f"Student Name: {student_name}")
            print(f"Average Grade: {average:.2f}")
            print(f"Final Grade: {letter_grade} {description}")
        else:
            print(f"No grades entered for {student_name}.")

        while True:
            continue_input = input("\nDo you want to enter grades for another student? [Y/N]: ").strip().upper()
            if continue_input in ['Y', 'N']:
                break
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

        if continue_input == 'N':
            break

if __name__ == "__main__":
    main()
