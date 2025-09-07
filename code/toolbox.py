import csv

class Portfolio:
    def __init__(self, company, price, share):
        self.company = company
        self.price = price
        self.share = share

    def stock_invest(self):
        invest = self.price * self.share
        return invest

    def total_invest(self, stock_invests):
        return sum(stock_invests)

class File:
    def __init__(self, path, row):
        self.path = path
        self.mode = 'w'
        self.row = row
        self.create_csv()

    def define_mode(self):
        mode = input('enter mode: (r/w/x/a)? ')
        return mode

    def add_row(self, row):
        self.mode = 'a'
        self.row = row

    def create_csv(self):
        try:
            with open(self.path, self.mode) as file:
                writer = csv.writer(file)
                writer.writerow(self.row)
        except FileExistsError:
            print('file already exists')
