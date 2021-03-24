
class Simulation:

    def __init__(self, fund, macd, signal):
        self.fund = fund
        self.macd = macd
        self.signal = signal
        self.shares_owned = 0

    def buy(self, shares_to_buy, current_price):
        self.fund -= shares_to_buy * current_price
        self.shares_owned += shares_to_buy

    def sell(self, shares_to_sell, current_price):
        self.fund += shares_to_sell * current_price
        self.shares_owned -= shares_to_sell

    def macd_transactions(self, traded_shares, data, starting_day):
        above = 0
        below = 0
        if self.macd[starting_day] - self.signal[starting_day] > 0:
            above = 1
        else:
            below = 1
        for i in range(starting_day+1, len(data)-1):
            if self.macd[i] - self.signal[i] > 0 and below:
                self.buy(traded_shares, data[i])
                below = 0
                above = 1
                print("saldo after buying: ",self.fund)
            elif self.macd[i] - self.signal[i] < 0 and above:
                self.sell(traded_shares, data[i])
                below = 1
                above = 0
                print("saldo after selling: ",self.fund)
        

