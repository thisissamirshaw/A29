#WAP to create a library with two methods like 
# issue book, return book
class lib:
    book_dict={'python':20,'Java':4,'sql':10,'django':35}

  
    def __init__(self, name,phno,sid,book=[]):
        self.name=name
        self.phno=phno
        self.sid=sid
        self.book=book    
        
def disp_obj(self):
    print(self.name,self.phno,self.sid,self.book)

def return_book(self):
    bn=input("Enter the rbook")
    self.book.remove(bn)
    self.book_dict[bn]+=1

obj=lib('pratik',3456787654,800)

print(lib.book_dict)
obj.disp_obj()
obj.issue_book()
obj.disp_obj()
print(lib.book_dict)
    

