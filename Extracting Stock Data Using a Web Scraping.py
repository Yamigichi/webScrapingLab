!pip install bs4

import pandas as pd
import requests
from bs4 import BeautifulSoup

#Use the requests library to download the webpage https://finance.yahoo.com/quote/AMZN/history?period1=1451606400&period2=1612137600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true. Save the text of the response as a variable named html_data
html_data=requests.get(" https://finance.yahoo.com/quote/AMZN/history?period1=1451606400&period2=1612137600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true.")

#Parse the html data using beautiful_soup.
beautiful_soup = BeautifulSoup(html_data.content,"html.parser")
print(beautiful_soup.prettify())

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    #Open = 
    Open = col[1].text
    #high =
    high= col[2].text
    #low =
    low= col[3].text
    #close =
    close= col[4].text
    #adj_close =
    adj_close= col[6].text
    #volume =
    volume=col[7].text
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
