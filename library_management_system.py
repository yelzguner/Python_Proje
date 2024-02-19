class Library:
#filename txt dosyasını yazacağımız yer olarak belirtilmeli.
    def __init__(self, filename="C:\\Users\\tikia\\OneDrive\\Masaüstü\\odev\\books.txt"):
        self.filename = filename

    def list_books(self):
        with open(self.filename, "r") as file:
            books = file.readlines()
            if not books:
                print("No books available.")
            else:
                print("List of Books:")
                for index, book in enumerate(books, start=1):
                    book_info = book.strip().split(',')
                    print(f"{index}) Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        with open(self.filename, "a") as file:
            file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        self.list_books()
        try:
            index = int(input("Enter the index of the book you want to remove: "))
            with open(self.filename, "r") as file:
                books = file.readlines()
            if 1 <= index <= len(books):
                del books[index - 1]  
                with open(self.filename, "w") as file:
                    file.writelines(books)  
                print("Book removed successfully.")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")



lib = Library()


while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")