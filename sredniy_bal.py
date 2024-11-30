grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students= sorted(students)
food=sum(grades[0])/len(students[0]),sum(grades[1])/len(students[1]),sum(grades[2])/len(students[2]),sum(grades[3])/len(students[3]),sum(grades[4])/len(students[4])
print(food)
klass={students[0]:food[0]},{students[1]:food[1]},{students[2]:food[2]},{students[3]:food[3]},{students[4]:food[4]}
print(klass)