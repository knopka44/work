import xml.etree.ElementTree as ET

tree = ET.parse("xml.xml")
root = tree.getroot()


def assertion(user_input):
    assert isinstance(user_input, str), f'{user_input} must be string'
    return True


def find_by_price(book_price):
    assertion(book_price)
    prices = [price.text for price in root.iter('price')]
    if book_price not in prices:
        print(f"Price {book_price} is not found")
    else:
        for book in root.iter('book'):
            if book.find('price').text == book_price:
                title = book.find('title').text
                author = book.find('author').text
                genre = book.find('genre').text
                publish_date = book.find('publish_date').text
                print(f"{title} by {author}\ngenre: {genre}\n"
                      f"price: {book_price}\npublish_date: {publish_date}\n")


def find_by_title(book_title):
    assertion(book_title)
    titles = [title.text for title in root.iter('title')]
    if book_title not in titles:
        print(f"Title {book_title} is not found")
    else:
        for book in root.iter('book'):
            if book_title == book.find('title').text:
                title = book.find('title').text
                author = book.find('author').text
                genre = book.find('genre').text
                price = book.find('price').text
                publish_date = book.find('publish_date').text
                print(f"{title} by {author}\ngenre: {genre}\n"
                      f"price: {price}\npublish_date: {publish_date}\n")


def find_by_author(book_author):
    assertion(book_author)
    if any([book_author in author.text for author in root.iter('author')]):
        for book in root.iter('book'):
            if book_author in book.find('author').text:
                title = book.find('title').text
                author = book.find('author').text
                genre = book.find('genre').text
                price = book.find('price').text
                publish_date = book.find('publish_date').text
                print(f"{title} by {author}\ngenre: {genre}\n"
                      f"price: {price}\npublish_date: {publish_date}\n")
    else:
        print(f"Author {book_author} is not found")


def find_by_description(book_description):
    assertion(book_description)
    descriptions = [description.text
                    for description in root.iter('description')]
    if book_description not in descriptions:
        print("Description is not found")
    else:
        for book in root.iter('book'):
            if book_description == book.find('description').text:
                match = book.find('title').text
                print(f"The book with the matching description is {match}")


find_by_price('36.75')
find_by_title('Maeve Ascendant')
find_by_author('Zed')
find_by_description('Even bad code can function. But if code isn’t clean, '
                    'it can bring a development organization to its knees.')
