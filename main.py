import streamlit as st
from src.database import Earnings, get_session, engine
from src.scraper import get_data

st.set_page_config(page_title="Earnings", layout="wide")
st.title("Earnings")
session = get_session()

try:

    earnings = Earnings.select_all(session)
    if not earnings:
        data = get_data()
        data.to_sql(name="earnings", con=engine, if_exists="append", index=False)
        st.dataframe(data)
    else:
        data = Earnings.select_dataframe(session)
        st.dataframe(data, hide_index=True)

    company_name = st.text_input("Company name")
    btn_search = st.button("Search")
    if btn_search:
        # Filter the DataFrame by company name
        result = data[data['company'] == company_name]

        # Check if any result is found
        if not result.empty:
            st.dataframe(result, hide_index=True)
        else:
            st.warning("No company found with that name.")

except Exception as ex:
    print(f"Something went wrong with error: {ex}")
finally:
    session.close()