# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

#-- Program Data --#

# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Variables
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data

#-- Processing --#
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    JHoward,11.17.2024,Created Class
    """

    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows
        :param file_name: string with the name of the file we are reading
        :param student_data: list of dictionary rows we are adding data to
        :return: list of dictionary rows filled with data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file from a list of dictionary rows

        :param file_name: string with the name of the file we are writing to
        :param student_data: list of dictionary rows containing student data
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

#-- Presentation (Input/Output) --#
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    """

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets data from the user and adds it to a list of dictionary rows
        :param student_data: list of dictionary rows containing our current data
        :return: list of dictionary rows filled with a new row of data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data.append({"FirstName": student_first_name, "LastName": student_last_name,"CourseName": course_name})
        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)  # Prints the custom message
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)
        return student_data

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user
        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message
        return choice

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the roster of students and courses they are registered for
        :return: None
        """
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in student_data:
            print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")
        print("-" * 50)
        print()

    #  End of class definitions

# Beginning of the main body of this script

#Load current json data
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new student data
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # Show all current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

print("Program Ended")