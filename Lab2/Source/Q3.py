
#class 1
class Person:

    #init constructor used
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)

#class 2(inherited)
class Student(Person):
    StudentCount = 0
    def __init__(self,name,email,student_id):
        Person.__init__(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        Person.display(self)
        print("Student Id: ",self.student_id)

#class 3 (inherited)
class Librarian(Person):
    StudentCount = 0
    def __init__(self,name,email,employee_id):
        #super call
        super().__init__(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Librarian Details:")
        Person.display(self)
        print("Employee Id is: ",self.employee_id)

#class 4
class Book():
    def __init__(self, bookname, author, book_id):
        self.book_name = bookname
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Details about the book")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)

#class 5
class Borrow_Book(Student,Book):
    def __init__(self, name, email, student_id, bookname, author, book_id):
        Student.__init__(self,name,email,student_id)
        Book.__init__(self, bookname, author, book_id)
    def display(self):
        print("Details of the borrowed book:")
        Student.display(self)
        Book.display(self)
Libdetails= []
Libdetails.append(Student('Namrata', 'namdutta@gmail.com', 1234))
Libdetails.append(Student('Pujita', 'pujitam@gmail.com', 4567))
Libdetails.append(Librarian('Librarian1', 'libemp1@gmail.com', 7777))
Libdetails.append(Librarian('Librarian2', 'libemp2@gmail.com', 4353))
Libdetails.append(Book('Python', 'Author1', 12311))
Libdetails.append(Book('Software Engg', 'Author2', 12312))
Libdetails.append(Borrow_Book('Namrata', 'namdutta@gmail.com', 1234, 'Python', 'Author1', 12311))
for obj, item in enumerate(Libdetails):
    item.display()
    print("\n")
    if obj == len(Libdetails)-1:
        item.displayCount()