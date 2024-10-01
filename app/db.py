import os

from sqlalchemy import create_engine, Column, Integer, String, text, Float, Boolean, false
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID

POSTGRES_HOST: str = os.environ['POSTGRES_HOST']
POSTGRES_PORT: str = os.environ['POSTGRES_PORT']
POSTGRES_USER: str = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB: str = os.environ['POSTGRES_DB']

# conection configuation
BATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(BATABASE_URL)

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    id = Column(UUID, primary_key=True, nullable=False, server_default=text("uuid_generate_v4()"))
    name = Column(String, server_default='')
    ean = Column(Integer, server_default='0')
    brand = Column(String, server_default='')
    full_price = Column(Float, server_default='0')
    discount_price = Column(Float, server_default='0')
    in_stock = Column(Boolean, server_default=false())
    url = Column(String, server_default='')
    url_img = Column(String, server_default='')


#create table
Base.metadata.create_all(engine)

#create session
Session = sessionmaker(bind=engine)
session = Session()

def insert_product(name, ean, full_price, discount_price, url, url_img):
    new_product = Products(name=name, ean=ean,
                           full_price=full_price,
                           discount_price=discount_price, url=url, url_img=url_img)
    session.add(new_product)
    session.commit()


# close session
session.close()
