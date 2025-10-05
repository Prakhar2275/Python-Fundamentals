class book:
    def __init__(self,title,author,copy):
        self.title=title
        self.author=author
        self.copy=copy
    
    def borrow_book(self):
        if self.copy>0:
            self.copy-=1
            print(f"You have borrowed:",self.title,"copies Left:",self.copy)
        else:
            print("No Copies of ",self.title,"are available")

    def return_book(self,title):
        self.copy+=1
        print("You have returned:",self.title,"copies Left:",self.copy)

    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Available Copies:",self.copy)

# some pre-added books for the library by prakhar

book1=book("Python Programming","John Doe",3)
book2=book("Data Science","Jane Smith",2)
book4=book("JS Programming","Tech Burner",10)
book3=book("Lana songs","Tailwinder",2)

# arrary for storing all the base names on books
books=[book1,book2,book3,book4]

# defining functions for the menu driven program


# function for borrowing  books form the library if choice is one
def choice_one():
    for i ,book in enumerate(books,start=1):
            print(f"{i}. {book.title} by {book.author},copies:{book.copy}")
    book_ch=int(input("Enter Book Number to Borrow:"))
    if 1<=book_ch<=len(books):
            books[book_ch-1].borrow_book()
    else:
        print("Invalid Book Number")


#  functions for returning books to library choice two

def choice_two():
    for i , book in enumerate(books, start =1):
            print(f"{i}.{book.title} by {book.author},copies:{book.copy}")
    book_ch=int(input("Enter the book Number To Return:"))
    if 1<=book_ch<=len(books):
                books[book_ch-1].return_book()
    else:
        print("Invalid Book Number")

# functions of showing the total available books in the library choice 3

def choice_three():
    print("\n Available Books:\n")
    for book in books:
            book.display()
            print("\n")


# for adding a new book to library and adding the base name to arry for the base names
def choice_four():
        base_name=input("Enter Base Name for the Book(book1 , book2):")
        title=input("Enter Book Title:")
        author=input("Enter Book Author:")
        copy=int(input("Enter Number of Copies:"))
        base_name=book(title,author,copy)
        books.append(base_name)

#  function for exiting form the library 

def choice_five():
        print("Exiting the Library System")


# menu driven structure and choices for the person who is visiting the library 

def menu():
    print("\n Library Menu")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. View Available  Book")
    print("4 Add Book")
    print("5. Exit")

# menu driven structure for using the library with choice giving and calling the functions form the various choices when called 

while True:
    menu()
    ch=int(input("Enter Your Choice:"))

    if ch==1:
        choice_one()
    elif ch==2:
        choice_two()
    elif ch==3:
        choice_three()
    elif ch==4:
         choice_four()
    elif ch==5:
        choice_five()
        break
    else: 
        print("Invalid Choice")




