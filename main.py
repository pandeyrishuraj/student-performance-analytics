"""
Student Performance Analytics System
EWB EduTech - Python with AI Mini Project

Run:
    python main.py

Requirements:
    pip install numpy pandas
"""

import numpy as np
import pandas as pd

DATA_FILE = "students.csv"
SUBJECT_COLUMNS = [
    "Python_Marks",
    "NumPy_Marks",
    "Pandas_Marks",
    "Data_Analysis_Marks",
]
PASS_MARKS = 40


def load_student_data(file_path=DATA_FILE):
    """Load student records from a CSV file using Pandas."""
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found. Keep it beside main.py.")
        return None

    required_columns = [
        "Student_ID", "Name", "Department",
        *SUBJECT_COLUMNS, "Attendance_Percent"
    ]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        print("Error: Missing required columns:", ", ".join(missing_columns))
        return None

    if data.empty:
        print("Error: The dataset is empty.")
        return None

    return data


def calculate_grade(average):
    """Return a grade based on the project's defined grading rule."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def process_student_data(data):
    """Calculate totals, averages, grades and pass/fail status."""
    data = data.copy()

    # NumPy is used for numerical calculations across the subject marks.
    marks_array = data[SUBJECT_COLUMNS].to_numpy(dtype=float)
    data["Total_Marks"] = np.sum(marks_array, axis=1)
    data["Average_Marks"] = np.round(np.mean(marks_array, axis=1), 2)

    # A student passes when they score at least 40 in every subject.
    data["Result"] = data[SUBJECT_COLUMNS].ge(PASS_MARKS).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )
    data["Grade"] = data["Average_Marks"].apply(calculate_grade)
    return data


def show_student_summary(data):
    """Display each student's total, average, grade and result."""
    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Percent"
    ]
    print("\n" + "=" * 92)
    print("STUDENT PERFORMANCE SUMMARY")
    print("=" * 92)
    print(data[display_columns].to_string(index=False))


def show_class_statistics(data):
    """Display class-level performance statistics."""
    averages = data["Average_Marks"].to_numpy()
    passed = int((data["Result"] == "Pass").sum())
    failed = int((data["Result"] == "Fail").sum())

    top_index = data["Average_Marks"].idxmax()
    low_index = data["Average_Marks"].idxmin()
    top_student = data.loc[top_index]
    low_student = data.loc[low_index]

    print("\n" + "=" * 55)
    print("CLASS PERFORMANCE STATISTICS")
    print("=" * 55)
    print(f"Total students             : {len(data)}")
    print(f"Class average              : {np.mean(averages):.2f}")
    print(f"Highest student average    : {top_student['Name']} ({top_student['Average_Marks']:.2f})")
    print(f"Lowest student average     : {low_student['Name']} ({low_student['Average_Marks']:.2f})")
    print(f"Students passed            : {passed}")
    print(f"Students failed            : {failed}")
    print(f"Pass percentage            : {(passed / len(data)) * 100:.2f}%")
    print(f"Average attendance         : {data['Attendance_Percent'].mean():.2f}%")


def show_subject_analysis(data):
    """Show average, highest and lowest marks for each subject."""
    print("\n" + "=" * 68)
    print("SUBJECT-WISE PERFORMANCE ANALYSIS")
    print("=" * 68)

    subject_summary = pd.DataFrame({
        "Subject": SUBJECT_COLUMNS,
        "Average_Marks": [data[column].mean() for column in SUBJECT_COLUMNS],
        "Highest_Marks": [data[column].max() for column in SUBJECT_COLUMNS],
        "Lowest_Marks": [data[column].min() for column in SUBJECT_COLUMNS],
    })
    subject_summary[["Average_Marks", "Highest_Marks", "Lowest_Marks"]] = (
        subject_summary[["Average_Marks", "Highest_Marks", "Lowest_Marks"]].round(2)
    )
    print(subject_summary.to_string(index=False))

    best_subject = subject_summary.loc[subject_summary["Average_Marks"].idxmax(), "Subject"]
    weakest_subject = subject_summary.loc[subject_summary["Average_Marks"].idxmin(), "Subject"]
    print(f"\nBest-performing subject   : {best_subject}")
    print(f"Subject needing attention : {weakest_subject}")


def show_top_performers(data, count=5):
    """Display the top students ranked by average marks."""
    top_students = data.nlargest(count, "Average_Marks")
    print("\n" + "=" * 55)
    print(f"TOP {min(count, len(data))} PERFORMING STUDENTS")
    print("=" * 55)
    print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))


def show_department_analysis(data):
    """Display average marks by department."""
    print("\n" + "=" * 55)
    print("DEPARTMENT-WISE AVERAGE")
    print("=" * 55)
    department_summary = (
        data.groupby("Department")["Average_Marks"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )
    print(department_summary.to_string())


def main():
    print("=" * 65)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    student_data = load_student_data()
    if student_data is None:
        return

    processed_data = process_student_data(student_data)
    show_student_summary(processed_data)
    show_class_statistics(processed_data)
    show_subject_analysis(processed_data)
    show_top_performers(processed_data)
    show_department_analysis(processed_data)

    # Save a copy of the analyzed data so the results can be reviewed later.
    processed_data.to_csv("student_performance_report.csv", index=False)
    print("\nReport saved to: student_performance_report.csv")
    print("Analysis completed successfully.")


if __name__ == "__main__":
    main()
