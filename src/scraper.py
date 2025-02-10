
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
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
            "EPS": td[2].text,
            "ForecastE": td[3].text,
            "Revenue": td[4].text,
            "ForecastR": td[5].text,
            "Market Cap": td[6].text,
            "Time": td[7].text
        }
        rows.append(data)
driver.quit()
print(rows)

data_df = pd.DataFrame(rows)
print(data_df)