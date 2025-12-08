import dataclasses


@dataclasses.dataclass
class Book:
    title: str
    author: str
    url: str


crime_dostoevsky = Book(
    "Преступление и наказание",
    "Федор Достоевский",
    "fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/"
)

invalid_book = Book(
    "748247428748274",
    "",
    ""
)
