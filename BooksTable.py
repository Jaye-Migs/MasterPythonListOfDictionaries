Books = {
  "ID" : 1,
  "Title" : "The Great Gatsby",
  "Author" : "F. Scott Fitzgerald",
  "Genre" : "Fiction",
  "Published Year" : 1925,
  "ISBN" : "978-0743273565",
  "Stock" : 20,
  "Price" : 15.99
},{
  "ID" : 2,
  "Title" : "To Kill a Mockingbird",
  "Author" : "Harper Lee",
  "Genre" : "Fiction",
  "Published Year" : 1960,
  "ISBN" : "978-0060935467",
  "Stock" : 35,
  "Price" : 10.99
},{
  "ID" : 3,
  "Title" : "1984",
  "Author" : "George Orwell",
  "Genre" : "Dystopian",
  "Published Year" : 1949,
  "ISBN" : "978-0451524935",
  "Stock" : 40,
  "Price" : 9.99
},{
  "ID" : 4,
  "Title" : "The Catcher in the Rye",
  "Author" : "J.D. Salinger",
  "Genre" : "Fiction",
  "Published Year" : 1951,
  "ISBN" : "978-0316769488",
  "Stock" : 25,
  "Price" : 8.99
},{
  "ID" : 5,
  "Title" : "A Brief History of Time",
  "Author" : "Stephen Hawking",
  "Genre" : "Non-Fiction",
  "Published Year" : 1988,
  "ISBN" : "978-0553380163",
  "Stock" : 10,
  "Price" : 18.99
}
for Book in Books:
    print(f"ID: {Book['ID']}, Title: {Book['Title']}, Author: {Book['Author']}, Genre: {Book['Genre']}, Published Year: {Book['Published Year']}, ISBN: {Book['ISBN']}, Stock {Book['Stock']}, Price: {Book['Price']}")