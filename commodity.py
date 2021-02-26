""" commodity.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 2/22/2021
Description:
Commodity class structure developed for tracking the price of
commodities (gold, silver, stocks, oil, etc.). Pricing data are 
read from /write to a JSON file."""

import json

class Commodity:
   
  def __init__(self, filename):
    self._create(self, filename)
    self._doesFileStorageExist(self, filename)
    self.uploadPriceHistory(self, filename)
    
  def getPriceOnThisDate(self, price, date):
  
  def setPriceOfToday(self, price, todayDate):
  
  def uploadPriceHistory(self, filename):
  
  def _doesFileStorageExist(self, filename):
  #TODO: if filename exists create file
  
  
