import csv
import pandas as pd

# Task 1
def write_excel_files():
    student_records = [
        {'Student ID': '2022-CS-677', 'Name': 'Muaaz Butt', 'Age': 20, 'Major' : 'Computer Science'},
        {'Student ID': '2022-CS-661', 'Name': 'Abdullah Ateeq', 'Age': 20, 'Major' : 'Computer Science'},
        {'Student ID': '2022-CS-703', 'Name': 'Naira', 'Age': 20, 'Major' : 'Computer Science'},
    ]
    
    student_grades = [
        {'Student ID': '2022-CS-677', 'Course': 'CS-101', 'Grade': 'A', 'credits' : 3}, 
        {'Student ID': '2022-CS-661', 'Course': 'CS-102', 'Grade': 'B+', 'credits' : 4}, 
        {'Student ID': '2022-CS-703', 'Course': 'CS-103', 'Grade': 'B+', 'credits' : 3}, 
    ]
    
    with pd.ExcelWriter('student_records.xlsx') as writer:
        pd.DataFrame(student_records).to_excel(writer, sheet_name='Records', index=False)
    
    with pd.ExcelWriter('student_grades.xlsx') as writer:
        pd.DataFrame(student_grades).to_excel(writer, sheet_name='Grades', index=False)
    
    print("Excel files have been created successfully.")

# Task 2
def read_excel_sheets(file_name):
    xl = pd.ExcelFile(file_name)
    for sheet_name in xl.sheet_names:
        df = xl.parse(sheet_name)
        print(f"Sheet: {sheet_name}")
        print(df.head(), "\n")    

# Task 3
def generate_timetable():
    timetable_data = {
        'Course' : ['CS-101', 'CS-101', 'CS-103', 'CS-103', 'CS-102', 'CS-102'],
        'Day' : ['Monday', 'Wednesday', 'Tuesday', 'Thursday', 'Friday', 'Wednesday'],
        'Time' : ['9:00 AM', '11:00 AM', '10:00 AM', '12:00 PM', '9:00 AM', '11:00 AM']
    }
    df = pd.DataFrame(timetable_data)
    print("Weekly Timetable")
    print(df)
    
# Task 4
def segregating_top_students(file_name):
    df = pd.read_excel(file_name, sheet_name='Grades')
    top_students = df[df['Grade'] == 'A']
    print("Top Students")
    print(top_students)
    
# Task 5
def calculate_gpa(file_name):
    df = pd.read_excel(file_name, sheet_name='Grades')
    
    # Define the grade point mapping
    grade_point_map = {'A': 4, 'B+': 3.5, 'B': 3, 'C': 2}
    
    # Map grades to grade points, with a default value of 0 for unknown grades
    df['Grade Points'] = df['Grade'].map(grade_point_map).fillna(0) * df['credits']
    
    # Calculate total points and total credits
    total_points = df['Grade Points'].sum()
    total_credits = df['credits'].sum()
    
    # Calculate GPA, handling the case where total_credits is zero
    if total_credits > 0:
        gpa = total_points / total_credits
    else:
        gpa = 0
    
    print(f"Calculated GPA: {gpa:.2f}")


if __name__ == "__main__":
    write_excel_files()
    read_excel_sheets('student_records.xlsx')  
    generate_timetable()
    segregating_top_students('student_grades.xlsx')  
    calculate_gpa('student_grades.xlsx')  
