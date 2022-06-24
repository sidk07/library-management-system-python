from operator import index
import my_functions
import os
my_functions.print_options()
(option) = input("Enter input and to exit enter 'x' ")
books = []
while (option != "x" and option != "X"):
    if option == '1':
        books.append(my_functions.create_book())
    elif option == '2':
        my_functions.save_books(books)
    elif option == '3':
        books = my_functions.load_books()
    elif option == '4':
        my_functions.issue_book(books)
        # print("The Book index is : " + str(my_functions.find_book(books, "1")))
    elif option == '5':
        my_functions.return_book(books)
    elif option == '6':
        my_functions.update_book(books)
    elif option == '7':
        my_functions.show_all_books(books)
    elif option == '8':
        my_functions.show_book(books)
    else:
        print("Enter values between 1 - 10")
    input("Press any key to proceed...")
    os.system("cls")
    my_functions.print_options()
    option = input()   

