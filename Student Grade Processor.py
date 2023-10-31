# Define a function to determine the letter grade based on numerical grade, student type, and curve score (if provided).
def determine_letter_grade(numerical_grade, student_type, curve_score):
    if curve_score is not None:
        # Calculate a curved numerical grade.
        max_numerical_grade = 100
        min_numerical_grade = 0
        numerical_grade = min_numerical_grade + ((numerical_grade / (curve_score - min_numerical_grade)) * (
                    max_numerical_grade - min_numerical_grade))
    # Check the student type and assign a letter grade based on numerical grade ranges.
    if student_type == "GRAD":
        if 95 <= numerical_grade:
            return 'H'
        elif 80 <= numerical_grade <= 94:
            return 'P'
        elif 70 <= numerical_grade <= 79:
            return 'L'
        else:
            return 'F'
    else:  # UNDERGRAD
        if 90 <= numerical_grade:
            return 'A'
        elif 80 <= numerical_grade <= 89:
            return 'B'
        elif 70 <= numerical_grade <= 79:
            return 'C'
        elif 60 <= numerical_grade <= 69:
            return 'D'
        else:
            return 'F'
# Define the main function.
def main():
    input_file_path = '/Users/vinodkumar/Desktop/vinod.txt'
    output_file_path = '/Users/vinodkumar/Desktop/vinod2.txt'
    # Ask the user if they want to curve the grades and set the 'curve' variable accordingly.
    curve_choice = input("Would you like to curve the grades? (Y/N) ").strip().lower()
    curve = curve_choice == 'y'
    # If curving is chosen, ask for the curve score; otherwise, set it to None.
    if curve:
        curve_score = float(input("Please enter the score that should map to a '100%' grade: "))
    else:
        curve_score = None

    try:
        # Read the input file containing student data.
        with open(input_file_path, 'r') as input_file:
            input_lines = input_file.readlines()

        students = []
        # Process student data from input file and determine letter grades.
        for i in range(0, len(input_lines), 3):
            student_type = input_lines[i].strip()
            student_name = input_lines[i + 1].strip()
            numerical_grade = int(input_lines[i + 2])

            letter_grade = determine_letter_grade(numerical_grade, student_type, curve_score)

            students.append(f"{student_name}\n{letter_grade}\n")

        # Write the processed data to an output file.
        with open(output_file_path, 'w') as output_file:
            for student_data in students:
                output_file.write(student_data)

        print("All data was successfully processed and saved to the requested output file.")

    except FileNotFoundError:
        print("The input file does not exist. Please check the file path and try again.")
    except ValueError:
        print("Error: Invalid numerical grade found in the input file.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Execute the main function if the script is run as the main module.
if __name__ == "__main__":
    main()
