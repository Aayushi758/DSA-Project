
class Student:
    def __init__(self, student_id, name, age, branch, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.branch = branch
        self.marks = marks
class Node:
    def __init__(self, student_record):
        self.data = student_record
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.undo_stack=[]
    def insert_beginning(self,student_record):
        new_node=Node(student_record)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        current=self.head
        while current is not None:
            record=current.data
            print("ID",record.student_id)
            print("NAME",record.name)
            print("AGE",record.age)
            print("BRANCH",record.branch)
            print("MARKS",record.marks)
            print("----------------")   
            current=current.next 

    def delete(self,student_id):
        if self.head is None:
            print("Empty List")
            return        

        if self.head.data.student_id==student_id:
            self.head=self.head.next
            
            print("------------")
            return
        current=self.head
        while current.next is not None:
            if current.next.data.student_id==student_id:
               deleted_record=current.next.data
               self.undo_stack.append(deleted_record)
               current.next=current.next.next
               
               print("----------------")
               return
            current=current.next

        print("Student not Found")


    def undo_delete(self):
        if len(self.undo_stack) == 0:
            print("Nothing to undo")
            return
        student_record = self.undo_stack.pop()
        self.insert_beginning(student_record)
        print("Deletion undone:", student_record.name)

