

req_bananas = 10

money = 5000

class shop:
    num_bananas = 20
    banana_price = 5

    def buy(self, req_bananas, money):
        total_cost = self.num_bananas * self.banana_price
        if self.num_bananas >= req_bananas and money >= self.banana_price:
            self.num_bananas -= req_bananas
            money -= total_cost
            print("You have successfully bought", req_bananas, "Bananas .The total price is", total_cost, "You have", money, "Dollars remaining")
        elif req_bananas > self.num_bananas:
            raise Exception("Purchase failed: Not enough bananas")
        elif self.num_bananas >= req_bananas and total_cost > money:
            raise Exception("Purchase failed: Not enough money")

purchase = shop()
print(purchase.buy(req_bananas, money))
