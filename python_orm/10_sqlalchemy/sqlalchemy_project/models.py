from sqlalchemy import create_engine

'''
<db_type>+<db_driver>://<user_name>:<password>@<host>:<port>/<db_name>
'''
CONNECTION_STRING = 'postgresql+psycopg2://postgres-user:password@localhost:5432/sqlalchemy_test'

engine = create_engine(CONNECTION_STRING)
