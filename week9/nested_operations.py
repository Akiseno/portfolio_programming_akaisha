grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for item in row:
        print(item)

print("--------------------------------")
print(grid[0][1])

#changing value of grid
grid[1][1] = 99
print(grid[1][1])

library_books = [
    ["The Great Gatsby", "F. Scott Fitzgerald", 180, "fiction"],
    ["1984", "George Orwell", 328, "comedy"],
    ["To Kill a Mockingbird", "Harper Lee", 281, "drama"]
]

for book in library_books:
    title = book[0]
    author = book[1]
    pages = book[2]
    genre = book[3]
    print(title, "by", author, "has", pages, "pages and is a", genre, "book")

#printing only certain type of books
print("--------------------------------")
for book in library_books:
    if book[3] == "fiction":
        print(book[0], "by", book[1], "has", book[2], "pages and is a", book[3], "book")

#finding longest paged book
print("--------------------------------")
longest_book = 0
longest_book_info = None
for book in library_books:
    if book[2] > longest_book:
        longest_book = book[2]
        longest_book_info = book
if longest_book_info:
    print(longest_book_info[0], "by", longest_book_info[1], "has", longest_book_info[2], "pages and is a", longest_book_info[3], "book")
print("The longest paged book is", longest_book)
