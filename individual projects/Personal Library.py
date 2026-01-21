# WH 2nd personal library program

#define a function named view to see the Books set takes set_to_view
def view(set_to_view):
    print("\033cYour books are:")
    #loop over set_to_view as i
    for i in set_to_view:
        #show i item 0 as italics then "by" i item 1
        print(f"\x1B[3m{i[0]}\x1B[0m by {i[1]}")
    input()

#define a function named add to add Books to the set takes set_to_add
def add(set_to_add):
    #ask the user for who the book is by set the vaule to by
    by = input("\033cWho is the book by?\n")
    #ask the user for the title of the book set the vaule to title
    title = input("What is the title?\n")
    #add a tuple with by and title to set_to_add
    set_to_add.add((title,by))
    return set_to_add

#define a function named remove to remove Books to the set takes set_to_remove
def remove(set_to_remove):
    while True:
        print("\033cYour books to remove are:")
        #set book_set to a list
        book_set = []
        #set count to 1
        count = 1
        #loop

        #loop over set_to_remove as i
        for i in set_to_remove:
            #add i to book_set
            book_set.append(i)
            #show count ":" show i item 0 as italics then "by" i item 1
            print(f"{count}: \x1B[3m{i[0]}\x1B[0m by {i[1]}")
            #add 1 to count
            count += 1
        print(f"{count}: exit")

        #ask the user for what book the want to remove set to want
        want = input("What book do you want to remove (as a number)?\n")
        #try
        try:
            if int(want) > 0: 
                if int(want) == count:
                    return set_to_remove
                else:
                    #set_to_remove pop book_set with want
                    set_to_remove.remove(book_set[int(want)-1])
                    return set_to_remove
        #else
        except:
            #pass
            pass

#define a function named find to find Books to the set takes set_to_finde
def find(set_to_finde):
    #loop
    while True:
        #ask the user if the want to search by Title or Author set as want
        want = input("\033cDo you wnat to search by\n1: title\n2: author?\n")
        #if want is Title
        if want.lower() == "title" or want == "1":
            #ask the user what the Title is set as title
            title = input("What title is it?\n")
            print("\033cThe books are:")
            #loop with set_to_finde as i
            for i in set_to_finde:
                #if title is in i itme 0
                if title in i[0]:
                    #show i item 0 as italics then "by" i item 1
                    print(f"\x1B[3m{i[0]}\x1B[0m by {i[1]}")
            input()
            break

        #if want is Author
        elif want.lower() == "author" or want == "2":
            #ask the user what the Author is set as author
            author = input("What author is it?\n")
            print(f"\033cThe books are:")
            #loop with set_to_finde as i
            for i in set_to_finde:
                #if author is in i item 1
                if author in i[1]:
                    #show i item 0 as italics then "by" i item 1
                    print(f"\x1B[3m{i[0]}\x1B[0m by {i[1]}")
            input()
            break

#define a function named personal_library that is the main menu
def personal_library():
    #set my_books to a set
    my_books = set()
    #loop
    while True:
        #ask the user if the want to see, add, remove, find, or exit. as want
        want =  input("\033cDo you want to:\n1: veiw your books\n2: add a book\n3: remove a book \n4: find a book \n5: exit\n")
        #if want is see
        if want == "1":
            #run veiw with my_books
            view(my_books)
        #if want is add
        elif want == "2":
            #run add with my_books
            add(my_books)
        #if want is remove
        elif want == "3":
            #run remove with my_books
            remove(my_books)
        #if want is find
        elif want == "4":
            #run find with my_books
            find(my_books)
        #if want is exit
        elif want == "5":
            #break out of the loop
            break

personal_library()