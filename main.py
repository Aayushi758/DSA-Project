from student import Node, Student,LinkedList
my_list=LinkedList()



s1 = Student(101, "Aditi", 20, "CSE-AI", 85)
s2 = Student(102, "Rahul", 19, "CSE", 90)
s3 = Student(103, "Priya", 20, "IT", 88)

my_list.insert_beginning(s1)
my_list.insert_beginning(s2)
my_list.insert_beginning(s3)

my_list.display()
print("Before Deletion")
print("                ")
my_list.display()

my_list.delete(102)
print("After Deletion")
print("                ")
my_list.display()

my_list.undo_delete()

print("After Undo")
my_list.display()
