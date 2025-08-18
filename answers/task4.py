import matplotlib.pyplot as plt  

houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
students = [50, 45, 40, 35]

# Vertical bar chart
plt.bar(houses, students)
plt.title("Students per House at Hogwarts")
plt.xlabel("Houses")
plt.ylabel("Number of Students")
plt.show()

# Horizontal bar chart
plt.barh(houses, students)
plt.title("Students per House (Horizontal View)")
plt.xlabel("Number of Students")
plt.ylabel("Houses")
plt.show()
