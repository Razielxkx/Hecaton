Earnings Calendar Scraper

Description

This project performs web scraping to extract financial data 
from an earnings calendar and stores it in a database for further analysis. 
The data includes information about companies, EPS (earnings per share), 
reported and estimated revenue, and market capitalization. 
The collected data is stored in a MySQL database, and a Streamlit-based graphical interface is used for visualization.
Technologies Used Additionally, 
Selenium is used for dynamic content extraction, and a Streamlit-based 
graphical interface is implemented for data visualization.

Project Structure

hecaton/
│── src/                 - Folder containing the scraper
│   │── scraper.py       - Web scraping script using Selenium
│   │── database.py      - Functions for MySQL database
│── env/                 - Virtual environment
│── .gitignore           - Git ignore file
│── main.py              - Main entry point of the project
│── requirements.txt     - List of dependencies
│── README.md            - Project documentation

Features

- Automated Web Scraping – Extracts financial data dynamically from an earnings calendar.
  - https://www.investing.com/earnings-calendar/

- Selenium Integration – Handles dynamic content loading for accurate data retrieval.

- Database Storage – Saves extracted data into MySQL.

- Streamlit  – Provides an interactive dashboard to visualize financial reports.

Technologies Used

- Python 3.9
- Selenium  – for data extraction

- MySQL – for data storage

- Pandas – for data processing and analysis

- Streamlit – for building the graphical user interface (GUI)


Installation and Configuration

1. Clone the Repository
- git clone https://github.com/user/repo.git
2. Create and Activate a Virtual Environment
- python -m venv venv
- venv\Scripts\activate
3. Install Dependencies
- pip install -r requirements.txt
4. Configure the MySQL Database
- Create a database and add the necessary table to store the extracted data
- create database Hecaton

 Usage

Launch the Streamlit Application

- streamlit run main.py
If you dont have the information in database the scraper will access the source website, extract data, and insert it into the MySQL database.

The application will open a web interface where you can view and filter the extracted data. 

License

- This project is distributed under the MIT license.
