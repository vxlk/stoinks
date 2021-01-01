from autoscraper import AutoScraper
import csv

# this is where the app will learn the rules for its scrapes

scraper = AutoScraper()

main_page = False
history = True

# ---------------------------------- Main Page ---------------------------------------------------------------
if main_page:
    url = 'https://finance.yahoo.com/quote/AAPL/'

    # price
    # Prev Close
    # Open
    # Bid (max)
    # Ask (min)
    # Day's Range
    # 52 Week Range
    # Volume
    # Avg. Volume
    # Fair Value
    # Market Cap
    # Beta
    # PE Ratio
    # EPS
    # Earnings Date
    # Forward Div Yield
    # Ex-Dividend Date
    # 1y Target
    wanted_list = ["133.72", "135.58", "133.76 x 2200", "133.75 x 1200", "133.40 - 135.99", "53.15 - 138.79", "92,882,124", "115,680,766", "Fair Value", "2.273T", "1.30", "40.77", "3.28", "Jan 26, 2021 - Feb 01, 2021", "0.82 (0.61%)", "Nov 06, 2020", "128.55"]

    # Here we can also pass html content via the html 
    # parameter instead of the url (html=html_content)

    # build new
    #result = scraper.build(url, wanted_list)
    # load old
    result = scraper.load(r"C:/Users/small/Desktop/stoinks/saved_models/yahoo_finance_main_page.json")
    result2 = scraper.get_result_exact('https://finance.yahoo.com/quote/MSFT/')
    result3 = scraper.get_result_exact('https://finance.yahoo.com/quote/TSLA/')

    #scraper.save(r"C:/Users/small/Desktop/stoinks/saved_models/yahoo_finance_main_page.json")
    print(result)
    print(result2)
    print(result3)

    # ---------------------------------- Main Page ---------------------------------------------------------------

if history:
    url = "https://finance.yahoo.com/quote/TSLA/history?p=TSLA"
# Date	Open	High	Low	Close*	Adj Close**	
    