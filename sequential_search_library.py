# mencari buku di perpusatakaan

def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()
    
    if title1[0] == title2[0]:
        return True
    
    return False

def sequential_search(books, book_title):
    for book in books:
        if is_similar(book['title'], book_title):
            return book['shelf']
        
    return "buku tidak ditemukan"

books = [
    {'title': 'python programming', 'shelf': 'A1'},
    {'title': 'data structures and algorithms', 'shelf': 'B2'},
    {'title': 'introduction to machine learning', 'shelf': 'C3'},
    {'title': 'database management system', 'shelf': 'D4'},
]

book_title = input("masukan judul buku yang ingin dicari: ")
shelf_location = sequential_search(books, book_title)
print(shelf_location)

#outputnya memasukan judul buku yang ingin dicari jika memasukan judul buku yang sudah tertera didalam syntax maka
#buku akan ditemukan, jika memasukan buku yang tidak ada didalam syntax maka output akan menampilkan buku tidak ditemukan