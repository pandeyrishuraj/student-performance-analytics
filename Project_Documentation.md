# Project Documentation
## Student Performance Analytics System

**Student Name:** Rishu Raj Pandey  
**College:** Career College, Bhopal  
**Course:** BCA, 5th Semester  
**Internship Domain:** Python with AI  
**Organization:** EWB EduTech Pvt. Ltd.

> Please verify and edit the student and college details before submission if any detail is incorrect.

## 1. Project Title
Student Performance Analytics System

## 2. Objective
The objective of this project is to create a Python-based system that reads student marks and attendance from a CSV file and analyzes academic performance. It calculates totals and averages, assigns grades, identifies pass/fail status, and reports class, subject, and department performance.

## 3. Technologies Used
- Python: program logic, functions, conditions, and file handling
- Pandas: reading CSV data, managing DataFrames, filtering, grouping, and summaries
- NumPy: numerical calculations such as total and average marks
- GitHub: hosting and sharing the source code and project files

## 4. Dataset Description
The project uses `students.csv`, a sample dataset containing 20 fictional student records. It includes Student ID, name, department, marks in Python, NumPy, Pandas and Data Analysis, and attendance percentage. Each subject mark is out of 100.

## 5. Implementation
1. **Load data:** Pandas reads `students.csv` into a DataFrame.
2. **Validate columns:** The program checks that required columns are present and that the dataset is not empty.
3. **Calculate total and average:** The subject marks are converted to a NumPy array. NumPy calculates each student's total and average.
4. **Assign grades:** A function assigns grades according to the average marks.
5. **Check pass/fail:** A student passes when their marks are at least 40 in every subject; otherwise, they fail.
6. **Analyze class performance:** The program calculates the class average, highest and lowest student averages, pass/fail counts, pass percentage, and average attendance.
7. **Analyze subjects:** The program calculates each subject's average, highest mark and lowest mark, then identifies the strongest and weakest subject averages.
8. **Find top performers:** Pandas selects the five students with the highest average marks.
9. **Analyze departments:** The program calculates average performance for each department.
10. **Save report:** The processed data is saved to `student_performance_report.csv`.

## 6. Key Features
- CSV dataset loading
- Student-wise total and average marks
- Automatic grade assignment
- Pass/fail classification
- Class-level statistics
- Subject-wise performance analysis
- Top-five student ranking
- Department-wise average
- Export of the processed report

## 7. Output / Screenshots
After running `python main.py`, capture screenshots of:
1. The student performance summary
2. Class performance statistics
3. Subject-wise performance analysis
4. Top-performing students and department-wise average

**Screenshot placeholders:** Add the screenshots here before final submission.

## 8. Final Outcome
The system processes the sample dataset and produces an organized summary of student performance. It helps identify high-performing students, subjects with higher or lower average marks, pass/fail counts, and department averages.

## 9. Challenges and Learning
This project provides practice in loading CSV data, organizing it with Pandas, performing numerical calculations with NumPy, writing functions, applying conditions, and summarizing data. While testing, check that the CSV file is in the same folder as `main.py`, that the required libraries are installed, and that the column names match the code.

## 10. GitHub Repository
**Repository URL:** Add your public GitHub repository URL here after uploading the project.

## Grading Rule Used
- A+: 90 and above
- A: 80 to less than 90
- B: 70 to less than 80
- C: 60 to less than 70
- D: 50 to less than 60
- F: below 50

A student passes only if every subject mark is at least 40. These rules are project examples; confirm with the trainer if official grading rules differ.
