""" commodity.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 2/22/2021
Description:
Commodity class structure developed for tracking the price of
commodities (gold, silver, stocks, oil, etc.) """


class Commodity:
  
  TODO: figure out how to read price history stored in a separate file 
  and how to upload new data to the file. dictionary priceRepository
  will be responsible for that.
  
  priceRepository = {}    #priceRepository is a dictionary
  
  def __init__(self, commodityType):
    self.commodityType = commodityType
    
  def getPriceHistory(self, dateRange, dateInterval = 1):
  
  def getPriceOnThisDate(self, price, date):
  
  def setPriceOfToday(self, price, todayDate):
  
  def uploadDictionaryOfPrices(self, filename):
  
