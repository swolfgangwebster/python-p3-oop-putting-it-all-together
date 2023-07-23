#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self._page_count = page_count

    def set_page(self, page):
        if type(page) != int:
            print("page_count must be an integer")
        self._page_count = page

    def get(self):
        return self._page_count

    page_count = property(get, set_page)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    
        