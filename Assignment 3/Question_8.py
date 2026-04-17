'''
Basic library management system with borrow, return and search using OOP and file handling.
'''

import csv

class Book:
    def __init__(self, bid, title, author, copies):
        self.bid = bid
        self.title = title
        self.author = author
        self.copies = int(copies)

class Library:
    def __init__(self):
        self.books = []
    def add(self, b):
        self.books.append(b)
    def search(self, title):
        for b in self.books:
            if title.lower() in b.title.lower():
                print("Found:", b.title, "Copies:", b.copies)
                return
        print("Not found")
    def borrow(self, title):
        for b in self.books:
            if title.lower() == b.title.lower() and b.copies > 0:
                b.copies -= 1
                print("Borrowed successfully")
                return
        print("Cannot borrow")

lib = Library()
lib.add(Book(1, "Python Basics", "John", 5))
lib.search("Python")
lib.borrow("Python")
