import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.investing.com/earnings-calendar/")

    table = driver.find_element(By.ID, "earningsCalendarData")

    headers = [th.text.strip() for th in table.find_elements(By.CSS_SELECTOR, "thead th")]
    rows = []
    for tr in table.find_elements(By.TAG_NAME, "tr"):
        td = tr.find_elements(By.TAG_NAME, "td")
        if len(td) > 1:
            data = {
                "company": td[1].text,
                "eps": td[2].text,
                "eps_forecast": td[3].text,
                "revenue": td[4].text,
                "revenue_forecast": td[5].text,
                "market_cap": td[6].text
            }
            rows.append(data)
    driver.quit()

    data_df = pd.DataFrame(rows)

    columns_to_check = ['eps', 'eps_forecast', 'revenue', 'revenue_forecast']
    data_df[columns_to_check] = data_df[columns_to_check].apply(lambda x: x.str.strip().str.replace('/  ', ''))

    filtered_df = data_df[~((data_df['eps'] == '--') &
                           (data_df['eps_forecast'] == '--') &
                           (data_df['revenue'] == '--') &
                           (data_df['revenue_forecast'] == '--'))]
    return filtered_df