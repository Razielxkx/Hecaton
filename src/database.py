import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()


def get_database_url():
    """Constructs the database URL from environment variables."""
    username = os.getenv("MYSQL_USERNAME")
    password = os.getenv("MYSQL_PASSWORD")
    host = "localhost"
    port = 3306
    database = "hecaton"
    return f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"


# Database setup
db_url = get_database_url()
engine = create_engine(db_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_session():
    """Creates and returns a new database session."""
    return Session()


class Earnings(Base):
    """Represents the earnings table in the database."""
    __tablename__ = "earnings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(50), nullable=False)
    eps = Column(String(20), nullable=True)
    eps_forecast = Column(String(20), nullable=True)
    revenue = Column(String(20), nullable=True)
    revenue_forecast = Column(String(20), nullable=True)
    market_cap = Column(String(50), nullable=True)


    @classmethod
    def select_all(cls, session):
        return session.query(Earnings).all()


    @classmethod
    def select_dataframe(cls, session):
        query = session.query(Earnings).all()
        columns = Earnings.__table__.columns.keys()
        df = pd.DataFrame([{col: getattr(row, col) for col in columns} for row in query])
        # df.drop(columns=["_sa_instance_state"], inplace=True)
        return df


    def __repr__(self):
        """Returns a string representation of the Earnings object."""
        return f"Company = {self.company}, EPS = {self.eps}, Revenue = {self.revenue}"


# Create database tables
Base.metadata.create_all(engine)

if __name__ == "__main__":
    session = get_session()
    try:
        Earnings.select_all(session)
        # Earnings.add_entry(session, "KFC", 5.2, "5.5B", 120, "125B", "2.5T")
        #
        # # Fetch and print all records
        # earnings_records = session.query(Earnings).all()
        # print(earnings_records)
    finally:
        session.close()
