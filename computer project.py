import mysql.connector as conn
mycon=conn.connect(host='localhost',user='root',password='1234')
if mycon.is_connected():
    print('connection is established')
cursor=mycon.cursor()
def borrow(bname1):
    #on interface user will click on show books
    avail=cursor.execute(""" here we write the syntax for show available books from tables""")
    
    if bname1 in (""" output list(avail)"""):
        #here we will have a table per user where we will add the new book to their list
        empty=cursor.execute(" if user1.IS_empty ")#so that only 1 book per user
        if empty is True:
            """ we have to change the  status in library to borrowed  and it to database of user
            who borrowed it, need help for this"""
    mycon.commit()

def insert(bname2):
    #insert new book to library(database)
    cursor.execute("insert into table library values (bname2)")
    mycon.commit()

def chavail(bname3):
    #in library database search for a new book
    books=cursor.execute("select * from library")
    if bname3 in books:
        print("the book is available")
    else:
        print("book is unavailable")
    mycon.commit()

def return:#i am not sure of the parameter
    """ on logging in user will be able to see the books he has borrowed
    then there will be a button on clicking it on the backhand"""
    # delete record from user1 table and add it to library table
    mycon.commit()

print("1=borrow")
print("2=insert")
print("3=check availibitly ")
print("4=return")
choice=int(input("enter what you want to  do"))
if choice==1:
    bname1=input(" enter the book name  you want: ")
    borrow(bname1)
if choice==2:
    bname2=input("enter the book name which you want to add")
    insert(bname2)
if choice==3:
    bname3=input("enter the book name which you to find")
    chavail(bname3)
if choice==4:
    # not sure what to add
