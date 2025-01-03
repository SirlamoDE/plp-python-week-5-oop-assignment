class Book:
    """
    Represents a book with attributes like title, author, and pages.
    """

    def __init__(self, title, author, pages, genre="Fiction"):
        """
        Constructor to initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
            genre (str, optional): The genre of the book. Defaults to "Fiction".
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def __str__(self):
        """
        Returns a string representation of the book object.
        """
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}"

    def display_info(self):
        """
        Displays the book information.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Genre: {self.genre}")


class Novel(Book):
    """
    Represents a novel, inheriting from the Book class.
    """

    def __init__(self, title, author, pages, genre="Fiction", publisher=""):
        """
        Constructor for the Novel class.

        Args:
            title (str): The title of the novel.
            author (str): The author of the novel.
            pages (int): The number of pages in the novel.
            genre (str, optional): The genre of the novel. Defaults to "Fiction".
            publisher (str, optional): The publisher of the novel. Defaults to an empty string.
        """
        super().__init__(title, author, pages, genre)  # Call the parent class constructor
        self.publisher = publisher

    def display_info(self):
        """
        Displays the book information (including publisher).
        """
        super().display_info()  # Call the parent class's display_info method
        print(f"Publisher: {self.publisher}")


# Create instances of the Book and Novel classes
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1170)
book1.display_info()

novel1 = Novel("The Great Gatsby", "F. Scott Fitzgerald", 192, "Classic", "Charles Scribner's Sons")
novel1.display_info()