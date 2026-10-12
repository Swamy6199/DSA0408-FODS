import numpy as np

student_scores = np.array([
    [80, 85, 90, 75],
    [70, 80, 85, 80],
    [90, 95, 80, 85],
    [85, 75, 90, 90]
])

avg = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

for i in range(4):
    print(subjects[i], "Average:", avg[i])

print("Highest Average Subject:", subjects[np.argmax(avg)])

