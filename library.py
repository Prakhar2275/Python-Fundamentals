class library:
    def __init__(self,title,author,copy):
        self.title=title
        self.author=author
        self.copy=copy
    
    def borrow_book(self,title):
        if self.copy>0:
            self.copy-=1
            print("You have borrowed:",title,"copies Left:",self.copy)
        else:
            print("No Copies of ",title,"are available")

    def return_book(self,title):
        self.copy+=1
        print("You have returned:",title,"copies Left:",self.copy)


