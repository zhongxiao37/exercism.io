class Library

  # Title;ISBN;Author;Published
  CATALOG_DATA = <<~DATA
    The Adventures of Tom Sawyer;9780191604928;Mark Twain;2007
    Republic;9780718198916;Plato;2012
    Programming Ruby: The Pragmatic Programmers Guide;9780974514055;David Thomas;2004
    Pride and Prejudice by Jane Austen;9781986431484;Jane Austen;2018
    To Kill a Mockingbird;9780446310789;Harper Lee;1988
    Cosmicomics;9780330319089;Italo Calvino;1969
    The Lord of the Rings;9780544003415;J. R. R. Tolkien;2012
    Lord of the Flies;9780140283334;William Golding;1999
    1984: A Novel;9780451524935;George Orwell;2009
  DATA
  
  class Book
    attr_accessor :title, :author, :publication_year, :isbn, :stock
  end
  
  def initialize
    @books = []
    CATALOG_DATA.split("\n").each do |b|
      data = b.split(';')
      book = Book.new
      book.title = data[0]
      book.isbn = data[1]
      book.author = data[2]
      book.publication_year = data[3]
      book.stock = 0
      @books << book
    end
  end
  
  [:title, :author, :publication_year, :stock].each do |m|
    define_method("lookup_#{m}") do |isbn|
      @books.find { |b| b.isbn == isbn }&.send(m)
    end
  end
  
  def add_stock!(isbn, stock)
    book = @books.find { |b| b.isbn == isbn }
    book.stock += stock if book
  end

  def book_in_stock?(isbn)
    book = @books.find { |b| b.isbn == isbn }
    book.stock.positive?
  end
  
end


p Library.new.lookup_publication_year("9780974514055")