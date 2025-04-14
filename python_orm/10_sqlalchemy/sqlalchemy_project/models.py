from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

'''
<db_type>+<db_driver>://<user_name>:<password>@<host>:<port>/<db_name>
'''
CONNECTION_STRING = 'postgresql+psycopg2://postgres-user:password@localhost:5432/sqlalchemy_test'

engine = create_engine(CONNECTION_STRING)
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False, default='Pencho')
    last_name = Column(String(30), nullable=False, default='Nechitankov')
    age = Column(Integer)
    salary = Column(Integer)







