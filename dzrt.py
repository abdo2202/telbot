Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:44:01) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
from bs4 import BeautifulSoup
import telegram
import schedule
import time

# Telegram bot credentials
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

# URL of the product or category page
URL = 'https://www.dzrt.com/product-url'

# Function to check product stock
def check_stock():
    response = requests.get(URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Finding stock information (This depends on the website's structure)
        stock_info = soup.find('span', class_='stock-status').get_text().strip()

        if 'In Stock' in stock_info:
            send_telegram_message(f"The product is back in stock! Check it out here: {URL}")
        else:
            print(f"Product still out of stock: {stock_info}")
    else:
        print(f"Failed to access {URL}")

# Function to send a message through Telegram
def send_telegram_message(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

# Schedule the stock check every 10 minutes
schedule.every(10).minutes.do(check_stock)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)