books = [
    dict(book_id=1001 ,title="Harry Potter", genre="fantasy" ,pages=500),
    dict(book_id=1002 ,title="A song of ice and Fire ", genre="fantasy" ,pages=700),
    dict(book_id=1003 ,title="1984", genre="classic" ,pages=800)
]

readers = [
    {"name":"gogo","borrowed":[1001,1003]},
    {"name":"momo","borrowed":[1002]},
    {"name":"yoyo","borrowed":[1001,1002]}
]

def books_by_genre(books, the_genre):
    selected_books = []
    total_pages = 0
    
    for book in books:
        if book["genre"] == the_genre:
            selected_books.append(book["title"])
            total_pages += book["pages"]
    
    average_pages = total_pages / len(selected_books) if selected_books else 0
    
    return (selected_books, average_pages)


def q1():
    result = books_by_genre(books, "fantasy")
    print(result)

def get_books_name_for_reader(books, readers, reader_name):
    borrowed_books_ids = []
    for reader in readers:
        if reader["name"] == reader_name:
            borrowed_books_ids = reader["borrowed"]
            break  
    
    borrowed_books_titles = []
    for book in books:
        if book["book_id"] in borrowed_books_ids:
            borrowed_books_titles.append(book["title"])
    
    return borrowed_books_titles

def q2():
    print(get_books_name_for_reader(books, readers, "gogo"))

def most_read_book(books, readers):
    book_count = {}

    for reader in readers:
        for book_id in reader["borrowed"]:
            book_count[book_id] = book_count.get(book_id,0)+1

    if not book_count:
        return set()
    
    max_count = max(book_count.values())
    
    most_read_ids = [book_id for book_id, count in book_count.items() if count == max_count]
    
    most_read_titles = set()
    for book in books:
        if book["book_id"] in most_read_ids:
            most_read_titles.add(book["title"])
    
    return most_read_titles

def q3():
    print(most_read_book(books, readers))

def loan_book(books, readers, reader_name, book_name):
    book_id = None
    for book in books:
        if book["title"] == book_name:
            book_id = book["book_id"]
            break
    if book_id is None:
        return False  
    
    for reader in readers:
        if reader["name"] == reader_name:
            if book_id in reader["borrowed"]:
                return False
            reader["borrowed"].append(book_id)
            return True
    
    return False

def q4():
    print(loan_book(books, readers, "momo", "1984"))  

def return_book(books, readers, reader_name, book_name):
    book_id = None
    for book in books:
        if book["title"] == book_name:
            book_id = book["book_id"]
            break
    if book_id is None:
        return False  

    for reader in readers:
        if reader["name"] == reader_name:
            if book_id in reader["borrowed"]:
                reader["borrowed"].remove(book_id)
                return True
            else:
                return False  

    return False

def readers_having_most_read_book(readers):
    book_count = {}
    
    for reader in readers:
        for book_id in reader["borrowed"]:
            book_count[book_id] = book_count.get(book_id, 0) + 1
    if not book_count:
        return set()
    max_count = max(book_count.values())
    most_read_books = {book_id for book_id, count in book_count.items() if count == max_count}
    readers_with_most_read = set()
    for reader in readers:
        for book_id in reader["borrowed"]:
            if book_id in most_read_books:
                readers_with_most_read.add(reader["name"])
                break
    return readers_with_most_read

def q5():
    pass

def q6():
    pass


def main():
    # q1()
    # q2()
    q3()
    # q4()
    q5()
    q6()



if __name__ == "__main__":
    main()