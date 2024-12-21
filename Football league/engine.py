from sqlalchemy import create_engine

SERVER = 'Tony\\SQLEXPRESS'
DATABASE = 'master'
DRIVER = 'Microsoft ODBC Driver 17 for SQL Server'
USERNAME = 'test'
PASSWORD = 'test'
DATABASE_CONNECTION = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/master?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
engine = create_engine(DATABASE_CONNECTION)