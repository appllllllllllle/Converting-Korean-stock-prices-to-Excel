import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


b = requests.get('https://finance.naver.com/sise/sise_market_sum.naver?&page=1')
soup = BeautifulSoup(b.content, 'html.parser')
stocks = soup.select('table.type_2 tr')
stock_data = []
for stock in stocks[2:102]:
    columns = stock.find_all('td')
    if len(columns) > 1:
        name = columns[1].get_text(strip=True)
        price = columns[2].get_text(strip=True)
        stock_data.append((name, price))
wb = Workbook()
ws = wb.active
ws.title = "주식 정보"
ws.append(["주식명", "주가"])
for stock in stock_data:
    ws.append([stock[0], stock[1]])
wb.save('주식.xlsx')
print("완료")
