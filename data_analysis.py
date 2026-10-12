
import pandas as pd
import matplotlib.pyplot as plt

# Sample student performance dataset
data = {
    "Student": ["Amit", "Priya", "Rahul", "Sneha", "Amit", "Kiran"],
    "Age": [19, 20, 19, None, 19, 21],
    "Marks": [85, 92, None, 78, 85, 88],
    "Attendance": [90, 95, 75, 80, 90, 88]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Data quality analysis
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Clean the dataset
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset:")
print(df)

# Exploratory Data Analysis
print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())
print("Average Attendance:", df["Attendance"].mean())

# Visualization
plt.figure(figsize=(7, 4))
plt.bar(df["Student"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_performance.png")
plt.show()

print("\nAnalysis completed successfully!")
