#importing class from code
from book import Book

import json

# print options
def print_options():
    print("Choose the specific option for that action ")
    print("1 - Create new book ")
    print("2 - Save book locally ")
    print("3 - Load books from disk ")
    print("4 - issue book ")
    print("5 - return book ")
    print("6 - update book ")
    print("7 - Show all books")
    print("8 - show book")
    print("x - To exit")

# creating book function
def input_book_info():
    id = input("ID : ")
    name = input("Name : ")
    description = input("Description : ")
    isbn = input("ISBN : ")
    page_count = int(input("Page Count : "))
    issued = input("Issued -> y/Y fro True, anything for False : ")
    issued = (issued == "y" or issued == "Y")
    author = input("Author : ")
    year = int(input("Year : "))
    return {
        'id' : id,
        'name' : name,
        'description' : description,
        'isbn' : isbn,
        'page_count' : page_count,
        'issued' : issued,
        'author' : author,
        'year' : year
    }

def create_book():
    print("Enter your book information ")
    book_input = input_book_info()
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    print(book.to_dict())
    return book

# save book function 
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
        try:
            file = open("books.dat", "w")
            file.write(json.dumps(json_books, indent = 4))
        except:
            print("Something went wrong while saving books...")

# loading book function
def load_books():
    try: 
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
            books.append(new_obj)
        print("Successfully loaded books...")
        return books 
    except:
        print("An error occur while loading book...")

# finding book function
# takes books and id of book to find
def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
    return None
    # print("Book not found...")

# issue book function 
# takes input as id and calls find_book function 
# sets issue value of book True or False
def issue_book(books):
    id = input("Enter book index you want to issue : ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book issued...")
    else:
        print("Book not found...")

#return book
def return_book(books):
    id = input("Enter book index you want to return : ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book returned...")
    else:
        print("Book not found...")

# update book function takes parameter as books
# asks for id input to find book
# if found creates a new book by already written function and book is replaced
# if book not found return not found
def update_book(books):
    id = input("Enter book ID you want to update : ")
    index = find_book(books, id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book updated...")
    else:
        print("Book not found...")

#show book function
#save all books function
def show_all_books(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input("Enter book index you are looking for : ")
    index = find_book(books, id)
    if index != None:
        # book = books[index].issued = False
        print(books[index].to_dict())
    else:
        print("Book not found...")
