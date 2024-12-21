from sqlalchemy import create_engine, text

SERVER = 'Tony\\SQLEXPRESS'
DATABASE = 'league'
DRIVER = 'Microsoft ODBC Driver 17 for SQL Server'
USERNAME = 'test'
PASSWORD = 'test'
DATABASE_CONNECTION = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
engine = create_engine(DATABASE_CONNECTION)