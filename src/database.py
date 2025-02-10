import os
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

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

    id = Column(Integer, primary_key=True)
    company = Column(String(50), nullable=False)
    eps = Column(DECIMAL, nullable=True)
    eps_forecast = Column(String(20), nullable=True)
    revenue = Column(DECIMAL, nullable=True)
    revenue_forecast = Column(String(20), nullable=True)
    market_cap = Column(String(50), nullable=True)

    @classmethod
    def add_entry(cls, session, company, eps, eps_forecast, revenue, revenue_forecast, market_cap):
        """Adds a new earnings entry to the database."""
        new_entry = cls(
            company=company,
            eps=eps,
            eps_forecast=eps_forecast,
            revenue=revenue,
            revenue_forecast=revenue_forecast,
            market_cap=market_cap
        )
        session.add(new_entry)
        session.commit()
        return new_entry

    def __repr__(self):
        """Returns a string representation of the Earnings object."""
        return f"Company = {self.company}, EPS = {self.eps}, Revenue = {self.revenue}"


# Create database tables
Base.metadata.create_all(engine)

if __name__ == "__main__":
    session = get_session()
    try:
        # Adding an example entry
        Earnings.add_entry(session, "KFC", 5.2, "5.5B", 120, "125B", "2.5T")

        # Fetch and print all records
        earnings_records = session.query(Earnings).all()
        print(earnings_records)
    finally:
        session.close()
