# Sales Profit Prdiction Calculation
# 28 September 2018
# CTI-110 P2T1 - Sales Prediction
# Jacob Barker
#

# ask user for projected amount of sales
# multiply projected sales by typical profit of 23%
# display the projected profits of the sales

def main():
    projectedSales = float(input("What are the projected sales amounts for this quarter? $"))
    projectedProfit = projectedSales*0.23
    print("The projected profits for this quarter are $", projectedProfit)
main()
