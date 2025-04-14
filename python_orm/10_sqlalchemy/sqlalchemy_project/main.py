import random

from sqlalchemy import or_

from models import engine, Employee, City

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

# session = Session()   # Not recommended
# session.close()

# with Session() as session:
    # # filter_by - only with =
    # employees = session.query(Employee).filter_by(age=20)
    # employees = session.query(Employee).filter(Employee.age > 40)

    # employees = session.query(Employee).where(
    #     # Employee.age >= 40, Employee.age <= 60  # AND
    #     # (Employee.age >= 30) | (Employee.salary > 6000),    # OR
    #     or_(Employee.age > 30, Employee.salary > 6000)
    # ). all() # makes it a list
    #
    # employees = session.query(Employee).filter(
    #     # Employee.first_name.startswith('A')
    #     Employee.first_name.like('An%')
    # )

    # # Get last employee. No last()
    # employee = session.query(Employee).order_by(Employee.id.desc()).first()
    # print(employee.first_name, employee.last_name)

    # # Update
    # employee = session.query(Employee).filter_by(id=1).first()
    # print(employee.first_name, employee.age)
    # employee.age = 70
    # session.commit()
    # employee = session.query(Employee).filter_by(id=1).first()
    # print(employee.first_name, employee.age)
    #
    # # Delete
    # employee = session.query(Employee).filter_by(id=1).first()
    # session.delete(employee)
    # session.commit()

# with Session() as session:
#     session.add_all((
#         City(name='Varna'),
#         City(name='Burgas'),
#         City(name='Primorsko'),
#         City(name='Sozopol'),
#         City(name='Tzarevo'),
#     ))
#     session.commit()

# with Session() as session:
#     employees = session.query(Employee).all()
#     for e in employees:
#     #     e.city_id = random.randint(1, 5)
#     # session.commit()
#         print(e.first_name, e.last_name, e.city.name)

# with Session() as session:
#     employees = session.query(Employee).filter(Employee.city_id==1).all()
#     for e in employees:
#         print(e.first_name, e.last_name, e.city.name)

# with Session() as session:
#     employees = session.query(Employee).filter(Employee.city.has(name='Sozopol')).all()
#     for e in employees:
#         print(e.first_name, e.last_name, e.city.name)

with Session() as session:
    # employees = session.query(Employee).filter(Employee.city.has(name='Sozopol')).all()

    # employees = session.query(Employee).join(City).filter(City.name=='Tzarevo')
    # for e in employees:
    #     print(e.first_name, e.last_name, e.city.name)

    # city = session.query(City).filter(City.name=='Burgas').first()
    # for e in city.employees:
    #     print(e.first_name, e.last_name, city.name)

    # city = session.query(City).order_by(City.name).all()
    # for c in city:
    #     for e in c.employees:
    #         print(e.first_name, e.last_name, c.name)

    employee = session.query(Employee).filter(Employee.id == 2).first()
    city = session.query(City).filter_by(id=employee.city_id).first()
    print(employee.first_name, employee.last_name, city.name)
