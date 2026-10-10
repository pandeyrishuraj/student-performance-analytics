# Student Performance Analytics System

**EWB EduTech | Python with AI Mini Project**

## 1. Project Objective
The Student Performance Analytics System reads student records from a CSV dataset, calculates marks and averages, assigns grades, identifies pass/fail status, and summarizes student, subject, and department performance.

## 2. Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset
- Git and GitHub (for version control and submission)

## 3. Dataset Description
`students.csv` contains 20 sample student records with these columns:
- `Student_ID`: Unique student identifier
- `Name`: Student name
- `Department`: Student department
- `Python_Marks`, `NumPy_Marks`, `Pandas_Marks`, `Data_Analysis_Marks`: Marks for four subjects, each out of 100
- `Attendance_Percent`: Attendance percentage

The dataset contains fictional sample data created for this academic project.

## 4. Grading and Pass/Fail Rules
The project uses the following sample grading rule:
- A+: average >= 90
- A: average >= 80 and < 90
- B: average >= 70 and < 80
- C: average >= 60 and < 70
- D: average >= 50 and < 60
- F: average < 50

A student is marked **Pass** only if they score at least 40 marks in every subject. Otherwise, the student is marked **Fail**. These are project-defined rules and can be changed if the trainer specifies a different rule.

## 5. Features
1. Reads student data using Pandas.
2. Uses NumPy to calculate total and average marks.
3. Uses a reusable grade function.
4. Uses conditions and loops/iteration through analysis operations.
5. Calculates class average, highest/lowest average, pass/fail count and pass percentage.
6. Produces subject-wise average, highest and lowest marks.
7. Lists the top five students by average marks.
8. Shows department-wise average performance.
9. Saves the processed results in `student_performance_report.csv`.

## 6. Project Structure
```text
student-performance-analytics/
├── main.py
├── students.csv
├── functions.py
├── README.md
└── Project_Documentation.md
```

`student_performance_report.csv` is generated after the program runs.

## 7. How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the required libraries:
   ```bash
   pip install numpy pandas
   ```
4. Run:
   ```bash
   python main.py
   ```
5. Review the terminal output and the generated `student_performance_report.csv`.

## 8. Expected Output
The program displays:
- A student summary table
- Overall class statistics
- Subject-wise performance
- Top five performers
- Department-wise averages

Exact values are calculated from `students.csv` when the program runs.

## 9. Learning Outcomes
This project demonstrates basic Python programming, CSV file handling, Pandas DataFrames, NumPy calculations, functions, conditional logic, sorting/ranking, grouping, and data analysis.

## 10. Limitations and Future Improvements
- The dataset is a sample dataset, not official college data.
- The grading and pass/fail thresholds are illustrative and should be adjusted to match any trainer-provided rules.
- A future version could add charts, input validation for marks, and a simple user interface.
