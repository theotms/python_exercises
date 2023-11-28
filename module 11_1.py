# Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each
# publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes. Create a print_information method to both subclasses for
# printing out all information of the publication in question. In the main program, create publications Donald Duck (
# chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both
# publications using the methods you implemented.

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"The publication name is {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"The name of the author is {self.author} and it has {self.page_count} pages.")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"The name of the chief editor is {self.chief_editor}")

publications = []
"""
don = Magazine("Donald Duck", "Aki Hyypä")
com = Book("Compartment No.6", "Rosa Liksom", 192)
don.print_information()
com.print_information()
"""

publications.append(Magazine("Donald Duck", "Aki Hyypä"))
publications.append(Book("Compartment No.6", "Rosa Liksom", 192))

for e in publications:
    e.print_information()
