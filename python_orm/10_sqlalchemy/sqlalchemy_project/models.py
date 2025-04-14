from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, Relationship

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

    city_id = Column(Integer, ForeignKey('cities.id'), default=1)
    city = Relationship('City', back_populates='employees')

    projects = Relationship('Project',
        secondary='employee_project_association',
        back_populates='employees'
    )


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    employees = Relationship('Employee', back_populates='city')


employee_project_association = Table(
    'employee_project',
    Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id'), primary_key=True),
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True)
)


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    employees = Relationship('Employee',
         secondary=employee_project_association,
         back_populates='projects'
    )
