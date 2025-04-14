from sqlalchemy import or_

from models import engine, Employee

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

# session = Session()   # Not recommended
# session.close()

with Session() as session:
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

    # Update
    employee = session.query(Employee).filter_by(id=1).first()
    print(employee.first_name, employee.age)
    employee.age = 70
    session.commit()
    employee = session.query(Employee).filter_by(id=1).first()
    print(employee.first_name, employee.age)

    # Delete
    employee = session.query(Employee).filter_by(id=1).first()
    session.delete(employee)
    session.commit()
