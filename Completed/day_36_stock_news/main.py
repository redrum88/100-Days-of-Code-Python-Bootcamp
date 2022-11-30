import requests
from twilio.rest import Client

# Global variables
account_sid = "YOUR TWILIO SID"  # Twilio SID
auth_token = "YOUR TWILIO AUTH KEY"  # Twilio Auth Key
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "YOUR ALPHA VANTAGE KEY"  # Alpha Vantage API Key
NEWS_KEY = "YOUR NEWS API KEY"   # News API Key
STOCK_ENDPOINT = "https://www.alphavantage.co/query"    # Stocks END Point
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"     # News END Point
from_number = "+14258421421"    # Enter your Twilio Phone Number
to_number = "+447759xxxxxx"     # Enter your Phone Number

# END POINT Parameters
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "1min",
    "apikey": STOCK_KEY
}

NEWS_PARAMETERS = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME
}
# Retrieve Stocks data
r = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_data = r.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# Retrieve yesterday and before yesterday closing price
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find difference between yesterday and before yesterday closing price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = (difference / float(yesterday_closing_price)) * 100

# If difference is more then 5% format text, send a msg with recent top 3 articles and data.
if abs(diff_percent) > 1:
    news_data = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news = news_data.json()
    articles = news["articles"]
    top_3_news = articles[:3]
    formatted_articles = [
        f"{STOCK}:{up_down}{round(diff_percent, 2)}% \nHeadline: {article['title']}. \nLink: {article['url']}" for
        article
        in
        top_3_news]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_=from_number,
            to=to_number
            )
        print(message.sid)
