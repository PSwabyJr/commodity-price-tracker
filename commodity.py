""" commodity.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 2/22/2021
Description:
Commodity class structure developed for tracking the price of
commodities (gold, silver, stocks, oil, etc.). Pricing data are 
read from /write to a JSON file."""

class Commodity:
  
  fileName= none   #file name that stores pricing data  
   
   def __init__(self):
      self._doesFileStorageExist(self)
   def getPriceOnThisDate(self, date):
      pass  
   def setPriceOfToday(self):
      pass  
   def getPriceHistory(self):   #get full price history recorded on file 
      pass  
   def _doesFileStorageExist(self):
      pass  
