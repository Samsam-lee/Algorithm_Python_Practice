coin = [500, 100, 50, 10]

def giveChange(price, money):
    tempChange = money - price
    for i in coin:
        tempChange -= tempChange//i*i
        print(tempChange)

giveChange(320, 1000)