books = []

while True:
    title = input("Enter the book title(type 'exit' to exit):")
    if title == 'end':
        break
    #Add a book to the list
    books.append(title)
    
print("Book list:", books)