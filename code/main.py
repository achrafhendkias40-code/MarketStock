# import database
from dataset import stock_prices
from toolbox import Portfolio, File

# create file
# save into a csv file
path = 'C:/Users/achra/output.csv'
data = ['company', 'stock price', 'shares', 'investment']
file = File(path, data)

# calculate investment at which company
investments = []
for company in stock_prices:
    stock_price = stock_prices[company]['price']
    shares = stock_prices[company]['shares']
    portfolio = Portfolio(company, stock_price, shares)
    final_price = portfolio.stock_invest()
    investments.append(final_price)

    # add data to file
    file.add_row([company, stock_price, shares, final_price])
    file.create_csv()
print('file successfully created\n\n')

# sum up investments
total_investment = round(sum(investments), 2)

# show total invest
print('your total investment is:',total_investment,'$')