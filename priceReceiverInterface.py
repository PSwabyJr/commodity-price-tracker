"""priceReceiverInterface.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 3/14/2021
Description:
Interface class used for communication between 3rd Party APIs and Commodity child classes

import metalsAPI
from metalsAPI import MetalsAPI
from datetime import datetime

class PriceReceiverInterface:
  
  tempData = {}    #dictionary used to store data to avoid repetitive API calls
  
  def __init__(self):
    self.apiRecipient = MetalsAPI()
  
  def getPricing(self, symbol):
    if bool(tempData):   #check to see if dictionary tempData has data  
      if self.tempData['date'] == datetime.today().strfttime('%Y-%m-%d'):  #date formatted in YYYY-MM-DD
        return 1/tempData[symbol]
    else:
      pricingData = self.apiRecipient.getPricing() 
      #storing data in a Dictionary tempData to avoid multiple API calls in the same hour
      self.tempData['date'] = pricingData['date']
      self.tempData['XAG'] = pricingData['XAG]
      self.tempData['XAU'] = pricingData['XAU']
      return 1/pricingData[symbol]
