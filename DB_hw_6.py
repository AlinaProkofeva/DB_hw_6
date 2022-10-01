import sys

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models_6 import create_tables, Publisher, Book, Shop, Stock, Sale

sql = 'postgresql'
login = 'postgres'
with open('C:\\Users\\Алина\\Desktop\\postgres_pass.txt', 'r') as f:
    passw = f.read()
server = 'localhost'
port = '5432'
db = 'db_hw5'

DSN = f'{sql}://{login}:{passw}@{server}:{port}/{db}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def show_publisher():
    command = input('Укажите название или идентификатор издателя: ')
    try:
        if int(command) in range (sys.maxsize**10):
            print(session.query(Publisher).filter(Publisher.id == command).all()[0])
    except:
        print(session.query(Publisher).filter(Publisher.name == command).all()[0])
    return

def find_shops():
    command = input('Укажите название издателя: ')
    res = session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == command).all()
    for i in res:
        print(i)


pub1 = Publisher(name='AST')
pub2 = Publisher(name='D&D')
session.add_all([pub1, pub2])
session.commit()

book1 = Book(title='Dragonlance', id_publisher=1)
book2 = Book(title='Dune', id_publisher=2)
shop1 = Shop(name='Litru')
shop2 = Shop(name='Bookva')
stock1 = Stock(id_book=1, id_shop=2, count=2)
stock2 = Stock(id_book=2, id_shop=2, count=1)
stock3 = Stock(id_book=1, id_shop=1, count=2)
session.add_all([book1, book2, shop1, shop2, stock1, stock2, stock3])
session.commit()

if __name__ == '__main__':
    show_publisher()
    find_shops()

session.close()