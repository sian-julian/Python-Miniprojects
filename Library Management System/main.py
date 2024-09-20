#admin section
def displaybook(books):
    if books:
        for i,book in enumerate(books,start=1):
            print(f"Book {i}")
            print(f"Book id: {book['id']}")
            print(f"Book Title: {book['title']}")
            print(f"Book Author: {book['author']}")
            print(f"book Quantity: {book['quantity']}")
            print()
    else:
        print("No Books Added!!")
        print()


def deletebook(books):
    id=input("Enter the book id to update:")
    found=False
    
    for i,book in enumerate(books):
        if book['id']==id:
            del books[i]
            print("Book Deleted Successfully!!")
            found=True
            break
    if found:
        print()
    else:
        print("Book not Found!!")



def updatebook(books):
    id=input("Enter the book id to update:")
    found=False
    
    for book in books:
        if book['id']==id:
            book['title']=input("Enter the New Book Title:")
            book['author']=input("Enter the New Author's Name:")
            book['quantity']=int(input("Enter the Updated Book Quantity:"))
            print("Book Updated Successfully!!")
            found=True
            break
    if found==True:
        print()
    else:
        print("Book Not Found!!")
        print()


def addbook(books):
    book={}
    while True:
        id=input("Enter the book id:")

        if any(book['id']==id for book in books):
                print("Id already exists....try another Id")
        else:
            book['id']=id
            break
    book['title']=input("Enter the Book Title:")
    book['author']=input("Enter the Author's Name:")
    book['quantity']=int(input("Enter the Book Quantity:"))
    books.append(book)
    print("Book Added Successfully!!")
    print()



def admin(admin_cred):
    print("**ADMIN PAGE**")
    admuser=input("Enter your Username:")
    adpass=input("Enter your password:")
    print()
    for admin1 in admin_cred:
        if admin1['username']==admuser and admin1['password']==adpass:
            print("WELCOME SIAN")
            print()
            admin_menu()
        else:
            print("INVALID CREDENTIALS!!")
            print()

def admin_menu():
    while True:
        print("**ADMIN MENU**")
        print("1.Add Book\n2.Update Book\n3.Delete Book\n4.Display All Books\n5.Exit from the admin menu\n")
        ch=int(input("Enter your choice:"))

        if ch==1:
            addbook(books)
        elif ch==2:
            updatebook(books)
        elif ch==3:
            deletebook(books)
        elif ch==4:
            displaybook(books)
        elif ch==5:
            print("Exiting from the Admin Menu...")
            print()
            break
        else:
            print("INVALID CHOICE!!....try again")
            print()

#user section

def register(users):
    user={}
    print("**USER REGISTRATION**")
    user['name']=input("Enter your Name:")
    user['age']=input("Enter your Age:")
    user['address']=input("Enter your Address:")
    while True:
        username=input("Enter a Username:")

        if any(user['uname']==username for user in users):
                print("Username already exists....try another Username")
        else:
            user['uname']=username
            break
            
    while True:
        phone=input("Enter your phone number:")

        if any(user['phoneno']==phone for user in users):
            print("Phone Number already exists....Try another phone")
        else:
            user['phoneno']=phone
            break
    
    user['pass']=input("Enter a Password:")
    users.append(user)
    print("User Registration Successfull!!")
    print()


def login(users,books):
    print("**LOGIN PAGE**")
    username=input("Enter your Username:")
    password=input("Enter your password:")

    for user in users:
        if user['uname']==username and user['pass']==password:
            print("WELCOME")
            print()
            usermenu(books)
        else:
            print("INVALID CREDENTIALS!!")
            print()
            break
    
def usermenu(books):
    while True:
        print("**USER MENU**")
        print("1.Display All Books\n2.Search Book by Name\n3.Exit from the User menu")
        ch=int(input("Enter your choice:"))
        print()

        if ch==1:
            displaybooks(books)
        elif ch==2:
            searchbook(books)
        elif ch==3:
            print("Exiting from the User Menu...")
            print()
            break
        else:
            print("INVALID CHOICE!!....try again")
            print()

def displaybooks(books):
    if books:
        for i,book in enumerate(books,start=1):
            # print(f"Book {i}")
            # print(f"Book id: {book['id']}")
            print(f"Book Title: {book['title']}")
            print(f"Book Author: {book['author']}")
            print(f"book Quantity: {book['quantity']}")
            print()
    else:
        print("No Books Added!!")
        print()

def searchbook(books):
    bname=input("Enter the Books Name you want to search:")
    found=False

    for book in books:
        if book['title']==bname:
            print(f"Book Title: {book['title']}")
            print(f"Book Author: {book['author']}")
            print(f"book Quantity: {book['quantity']}")
            found=True
            print()
            break
    if found:
        print()
    else:
        print("Book not Found!!")
        print()

def user():
    while True:
        print("**USER SECTION**")
        print("1.Registration\n2.Login\n3.Exit\n")
        ch=int(input("Enter your choice:"))
        print()

        if ch==1:
            register(users)
        elif ch==2:
            login(users,books)
        elif ch==3:
            print("Exiting From the User Menu....")
            print()
            break  
        else:
            print("INVLAID CHOICE!!...try again") 
            print()    

#Main Section

admin_cred=[]
admin1={}
admin1['username']="sian"
admin1['password']="1234"
admin_cred.append(admin1)
books=[]
users=[]

while True:
    print("***LIBRARY MANAGEMENT SYSTEM***")
    print("1.Admin\n2.User\n3.Exit")
    ch=int(input("Enter your choice:"))
    print()

    if ch==1:
        admin(admin_cred)
    elif ch==2:
        user()
    elif ch==3:
        print("Exiting from the program...")
        break
    else:
        print("INVALID CHOICE!!....try again")

