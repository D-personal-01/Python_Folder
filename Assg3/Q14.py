''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
14. Using Matplotlib, create a bar graph showing the number of students in five different departments of a college. Provide proper labels and title. '''

import matplotlib.pyplot as plt

dept = ["BCA", "BBA", "B.Com", "B.Sc", "BJMC"]
stud = [120, 95, 80, 110, 85]

plt.bar(dept, stud, color="skyblue", edgecolor="navy")

plt.xlabel("Departments")
plt.ylabel("Number of Students")
plt.title("Number of Students in Different Departments")

plt.show()
