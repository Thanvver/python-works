class Book:
    book_name=str
    author=str
    price=int
    pages=int

    def __init__(self,book_name,author,price,pages):
        
        self.book_name=book_name
        self.author=author
        self.price=price
        self.pages=pages

    def get(self):
        print(self.book_name,self.author,self.price,self.pages)

    def __str__(self):
        return self.book_name+self.author+str(self.price)+str(self.pages)
        


obj1=Book("adujeevitham","benyamin",750, 600)
print(obj1)


obj2=Book("harrypotter","jk rowling",2500,4300)
print(obj2)